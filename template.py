import os
from pathlib import Path
import logging

project_name = "readme_gen"

list_of_files = [
    f"{project_name}/__init__.py",

    f"{project_name}/parser/__init__.py",
    f"{project_name}/parser/github_parser.py",
    f"{project_name}/parser/local_parser.py",

    f"{project_name}/collector/__init__.py",
    f"{project_name}/collector/data_reader.py",

    f"{project_name}/generator/__init__.py",
    f"{project_name}/generator/content_writer.py",
    f"{project_name}/generator/content_formatter.py",

    f"{project_name}/templates/__init__.py",
    f"{project_name}/templates/default.md.jinja",

    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_local_parser.py",
    f"{project_name}/tests/test_github_parser.py",

    f"{project_name}/temp_project_directory/project_requirements.txt",
    f"{project_name}/temp_project_directory/project_structure.txt",

    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/utils.py",

    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Creating directory: {file_dir}")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")