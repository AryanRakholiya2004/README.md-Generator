from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from dataclasses import dataclass
from readme_gen.utils import build_file_tree

@dataclass
class ContentFormatterConfig:
    template_dir: str = str(Path(__file__).resolve().parent.parent / "templates")
    template_name: str = "default.md.jinja"

class ContentFormatter:
    def __init__(self):
        self.config = ContentFormatterConfig()
        self.env = Environment(loader=FileSystemLoader(self.config.template_dir))
        self.metadata = {}

    def normalize_languages(self, extensions):
        """
        Convert file extensions to actual language names and filter out unnecessary ones.
        
        Args:
            extensions: List of file extensions with dots (e.g., ['.py', '.md', '.jinja', '.txt'])
        
        Returns:
            List of actual language names (e.g., ['python', 'jinja2'])
        """
        # Mapping of file extensions to actual language names
        extension_to_language = {
            '.py': 'python',
            '.jinja': 'jinja2',
            '.html': 'html',
            '.js': 'javascript',
            '.css': 'css',
            '.cpp': 'c++',
            '.c': 'c',
            '.java': 'java',
            '.rs': 'rust',
            '.go': 'go',
            '.ts': 'typescript',
            '.rb': 'ruby',
            '.php': 'php',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.sh': 'shell',
            '.sql': 'sql',
            '.r': 'r',
            '.jsx': 'react',
            '.tsx': 'react typescript',
            '.vue': 'vue',
            '.dart': 'dart',
            '.lua': 'lua',
            '.ex': 'elixir',
            '.exs': 'elixir',
            '.hs': 'haskell',
            '.yml': 'yaml',
            '.yaml': 'yaml',
            '.json': 'json',
            '.xml': 'xml',
            '.cs': 'c#',
            '.fs': 'f#',
            '.pl': 'perl',
            '.pm': 'perl',
            '.ipynb': 'jupyter notebook',
        }
        
        # List of extensions to exclude (documentation, config, etc.)
        exclude_extensions = ['.md', '.txt', '.csv', '.log', '.gitignore', '.env', '.LICENSE']
        
        # Process the extensions
        normalized_languages = set()
        for ext in extensions:
            # Skip excluded extensions
            if ext.lower() in exclude_extensions:
                continue
            
            # Convert to language or keep original if not in mapping
            language = extension_to_language.get(ext.lower(), ext.lstrip('.').lower())
            normalized_languages.add(language)

        return sorted(list(normalized_languages))

    def generate_readme(self, metadata: dict) -> str:
        # template_dir = Path(__file__).resolve().parent.parent / "templates"
        env = Environment(loader=FileSystemLoader(self.config.template_dir),trim_blocks=True,lstrip_blocks=True)

        # Converting file extensions to actual language names
        metadata['languages'] = self.normalize_languages(metadata['languages'])
        self.metadata = metadata

        env.globals['build_file_tree'] = build_file_tree
    
        template = env.get_template(self.config.template_name)
        metadata['file_tree'] = build_file_tree(metadata['files'])
        output = template.render(**metadata)
        return output