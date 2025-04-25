from dataclasses import dataclass
from readme_gen.logger import logging
from readme_gen.generator.content_formatter import ContentFormatter
from pathlib import Path
import os

@dataclass
class DataReaderConfig:
    project_dir: str = str(Path(__file__).resolve().parent.parent / "temp_project_directory/cloned_projects")
    requirements_file_path: str = str(Path(project_dir).resolve() / "project_requirements.txt")

class DataReader:
    def __init__(self):
        logging.info("Initializing DataReader...")
        self.config = DataReaderConfig()

    def requirement_collector(self,metadata : dict):
        if metadata['has_requirements']:
            logging.info("Collecting requirements from requirements.txt...")

            print(self.config.requirements_file_path)
            print(self.config.project_dir)
            requirements_path = os.path.join(self.config.project_dir, metadata['project_name'], "requirements.txt")
            with open(requirements_path, 'r', encoding='utf-8') as f:
                requirements = f.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            metadata['requirements'] = requirements
            print(requirements)
            with open(self.config.requirements_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(requirements))

            return metadata

        else:
            logging.info("Collecting requirements from Python files...")

            requirements = []
            for file in metadata['files']:
                if file.endswith('.py'):
                    with open(file, 'r', encoding='utf-8') as f:
                        file_content += f.readlines()
                        requirements = file_content.findall('import ')
                        print(requirements)