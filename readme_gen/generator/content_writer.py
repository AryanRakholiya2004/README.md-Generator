from dataclasses import dataclass
from pathlib import Path
import google.generativeai as genai

@dataclass
class ContentWriterConfig:
    project_dir: str = str(Path(__file__).resolve().parent.parent / "temp_project_directory/cloned_projects")
    requirements_file_path: str = str(Path(project_dir).resolve() / "project_requirements.txt")

    # Ollama model config
    model_name: str = "gemma2:2b"
    system_prompt: str = "You are a helpful assistant. You will be given a project metadata and you will generate a project description based on it, in one paragraph."

class ContentWriter:
    def __init__(self):
        self.config = ContentWriterConfig()
        self.requirements = []

    def save_requirement_txt(self, requirements: list):
        """
        Save the requirements to a requirements.txt file.
        """
        with open(self.config.requirements_file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(requirements))

    def project_description_write(self, metadata: dict, api_key_input: str):
        # Initialize the Ollama
        user_prompt = f"Generate a engaging project description based on the following metadata: {metadata}"

        # Generate project description using the metadata
        genai.configure(api_key=api_key_input)
        model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite',system_instruction=self.config.system_prompt)

        # Generate project description using the metadata
        response = model.generate_content(user_prompt)
        generated_description = response.text
        print(generated_description)

        # Write the generated description to a file
        description_file_path = Path(self.config.project_dir) / "project_description.txt"
        with open(description_file_path, 'w', encoding='utf-8') as f:
            f.write(generated_description)