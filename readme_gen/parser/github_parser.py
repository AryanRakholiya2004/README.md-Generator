import os
from dataclasses import dataclass
from readme_gen.logger import logging
from git import Repo
from pathlib import Path


@dataclass
class GitHubParserConfig:
    temp_dir_base: str = str(Path(__file__).resolve().parent.parent / "temp_project_directory" / "cloned_projects")


class GitHubParser:
    def __init__(self):
        logging.info("Initializing GitHubParser...")
        self.base_temp_path = GitHubParserConfig.temp_dir_base
        self.project_name = ''
        self.dir_ignore_patterns = ['.git', '__pycache__', '.idea', '.vscode', '.DS_Store']
        self.file_ignore_names = ['.gitignore', '.gitattributes']

    def is_ignored(self, path: str) -> bool:
        # Ignore if any part of the path contains an ignored directory
        for pattern in self.dir_ignore_patterns:
            if pattern in Path(path).parts:
                return True
        return False

    def parse_repo(self, repo_url: str):
        try:
            logging.info("Parsing GitHub repository...")
            print("📦 Cloning repository...")

            # Create unique directory for cloning
            counter = 1
            repo_name = Path(repo_url).stem
            clone_path = os.path.join(self.base_temp_path, repo_name)

            while os.path.exists(clone_path):
                clone_path = os.path.join(self.base_temp_path, f"{repo_name}_{counter}")
                counter += 1

            Repo.clone_from(repo_url, clone_path)
            self.project_name = repo_name

            metadata = {
                "project_name": self.project_name,
                "files": [],
                "directories": [],
                "has_readme": False,
                "has_license": False,
                "has_requirements": False,
                "languages": set()
            }

            for root, dirs, files in os.walk(clone_path):
                rel_root = os.path.relpath(root, clone_path)

                if self.is_ignored(root):
                    continue

                if rel_root != '.':
                    metadata["directories"].append(rel_root)

                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, clone_path)

                    if self.is_ignored(file_path) or file in self.file_ignore_names:
                        continue

                    metadata["files"].append(rel_path)

                    if file.lower() == "readme.md":
                        metadata["has_readme"] = True
                    elif file.lower() == "license":
                        metadata["has_license"] = True
                    elif file.lower() == "requirements.txt":
                        metadata["has_requirements"] = True

                    # Language detection
                    ext = os.path.splitext(file)[1]
                    if ext:
                        metadata["languages"].add(ext.lower())

            metadata["languages"] = list(metadata["languages"])

            print("✅ Repository cloned and parsed successfully!")
            logging.info("Repository cloned and parsed successfully!")
            return metadata

        except Exception as e:
            print(f"❌ Error: {e}")
            raise RuntimeError(f"Failed to parse GitHub repo: {e}")
