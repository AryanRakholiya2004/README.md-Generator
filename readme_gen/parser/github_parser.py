import os
import shutil
import tempfile
from dataclasses import dataclass
from git import Repo
from pathlib import Path

@dataclass
class GitHubParserConfig:
    temp_dir_path: str = str(Path(__file__).resolve().parent.parent / "temp_project_directory/clone_projects")

class GitHubParser:
    def __init__(self):
        self.temp_dir_path = GitHubParserConfig.temp_dir_path
        self.project_name = ''
        self.ignore_list = ['.git', '__pycache__', '.idea', '.vscode', '.DS_Store']

    def parse_repo(self, repo_url: str):
        try:
            print("📦 Cloning repository...")

            # Ensure unique directory for cloning
            clone_dir = os.path.join(self.temp_dir_path, Path(repo_url).stem)
            counter = 1
            while os.path.exists(clone_dir):
                clone_dir = os.path.join(self.temp_dir_path, f"{Path(repo_url).stem}_{counter}")
                counter += 1

            Repo.clone_from(repo_url, clone_dir)
            self.temp_dir_path = clone_dir  # Update temp_dir_path to point to the actual cloned directory

            # Get project name
            self.project_name = Path(repo_url).stem

            # Extract metadata
            metadata = {
                "project_name": self.project_name,
                "files": [],
                "directories": [],
                "has_readme": False,
                "has_license": False,
                "has_requirements": False,
                "languages": set()
            }



            for root, dirs, files in os.walk(self.temp_dir_path):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    metadata["directories"].append(os.path.relpath(dir_path, self.temp_dir_path))

                for file in files:
                    file_path = os.path.join(root, file)
                    metadata["files"].append(os.path.relpath(file_path, self.temp_dir_path))

                    if file.lower() == "readme.md":
                        metadata["has_readme"] = True
                    if file.lower() == "license":
                        metadata["has_license"] = True
                    if file.lower() == "requirements.txt":
                        metadata["has_requirements"] = True

                    # Language detection based on file extension
                    ext = os.path.splitext(file)[1]
                    if ext:
                        metadata["languages"].add(ext.lower())

            metadata["languages"] = list(metadata["languages"])

            print("✅ Repository cloned successfully !")
            return metadata

        except Exception as e:
            print(f"Error: {e}")
            raise RuntimeError(f"Failed to parse GitHub repo: {e}")
