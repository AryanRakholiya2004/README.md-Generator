from dataclasses import dataclass
from readme_gen.logger import logging
from pathlib import Path
import os
import re
from bs4 import BeautifulSoup
from ast import parse, Import, ImportFrom

@dataclass
class DataReaderConfig:
    project_dir: str = str(Path(__file__).resolve().parent.parent / "temp_project_directory/cloned_projects")
    requirements_file_path: str = str(Path(project_dir).resolve() / "project_requirements.txt")

class DataReader:
    def __init__(self):
        logging.info("Initializing DataReader...")
        print("Initializing DataReader...")
        self.config = DataReaderConfig()
        self.requirements = []
        self.lib_ignore_list = [
            'abc', 'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore', 'atexit', 'audioop', 'base64', 'binascii', 'binhex', 'bisect', 'builtins', 'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorsys', 'compileall', 'concurrent', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'cProfile', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils', 'doctest', 'email', 'encodings', 'ensurepip', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput', 'fnmatch', 'fractions', 'ftplib', 'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'imaplib', 'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword', 'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'msilib', 'multiprocessing', 'netrc', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'ossaudiodev', 'parser', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib', 'posix', 'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'termios', 'textwrap', 'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'types', 'typing', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound', 'wsgiref', 'xdrlib', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib', 'git', 'curl', 'wget', 'ssh', 'scp', 'rsync', 'tar', 'gzip', 'gunzip', 'unzip', 'zip', 'make', 'gcc', 'g++', 'cmake', 'vim', 'nano', 'htop', 'systemctl', 'docker', 'docker-compose', 'kubectl', 'ffmpeg', 'nmap', 'iptables', 'ufw', 'tmux', 'screen', 'ps', 'kill', 'top', 'grep', 'sed', 'awk', 'ls', 'cat', 'chmod', 'chown', 'find', 'locate', 'mount', 'umount', 'df', 'du', 'fdisk', 'parted', 'lsof', 'strace', 'dmesg', 'journalctl', 'python', 'pip', 'node', 'npm', 'yarn', 'java', 'javac', 'ruby', 'perl', 'php', 'composer', 'mongod', 'mysql', 'psql', 'sqlite3', 'redis-server', 'memcached', 'ansible', 'terraform', 'vagrant'
        ]

    def _is_project_module(self, module_name, project_name):
        """
        Check if a module is likely a project-specific module.
        
        This checks:
        1. If the module name starts with the project name
        2. If the module name contains internal project structure indicators
        """
        # Check if module name starts with project name (case insensitive)
        if project_name and module_name.lower().startswith(project_name.lower()):
            return True
        if '.' in module_name:
            return True
            
        return False

    def requirement_collector(self,metadata : dict):
        if metadata['has_requirements']:
            logging.info("Collecting requirements from requirements.txt...")
            print("Collecting requirements from requirements.txt...")

            print(self.config.requirements_file_path)
            requirements_path = os.path.join(self.config.project_dir, metadata['project_name'], "requirements.txt")
            with open(requirements_path, 'r', encoding='utf-8') as f:
                self.requirements = f.readlines()
            self.requirements = [req.strip() for req in self.requirements if req.strip()]
            metadata['requirements'] = self.requirements
            print(self.requirements)
            with open(self.config.requirements_file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.requirements))

        logging.info("Collecting requirements from Python files...")
        print("Collecting requirements from Python files...")

        file_content = ""
        for file in metadata['files']:
            if file.endswith('.py'):
                file_path = os.path.join(self.config.project_dir, metadata['project_name'], file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.readlines()

                    # Parse the Python file content to extract imports
                    imports = []
                    try:
                        tree = parse(''.join(file_content))
                        for node in tree.body:
                            if isinstance(node, Import):
                                imports.extend(alias.name for alias in node.names)
                            elif isinstance(node, ImportFrom):
                                if node.module:
                                    imports.append(node.module)
                    except Exception as e:
                        logging.error(f"Error parsing file {file}: {e}")
                        print(f"Error parsing file {file}: {e}")

                    # Use BeautifulSoup to process the file content (if needed for other purposes)
                    soup = BeautifulSoup(''.join(file_content), 'html.parser')
                    # Example: Extract comments or other text if necessary
                    comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('#'))
                    # print(f"Found imports: {imports}")
                    self.requirements.extend(imports)

        # Remove duplicates and sort the requirements
        self.requirements = sorted(set(self.requirements))
        self.requirements = [req for req in self.requirements if req not in self.lib_ignore_list]
        self.requirements = [req for req in self.requirements if not self._is_project_module(req, metadata['project_name'])]

        logging.info("Requirements collected successfully.")

        # saving into metadata
        metadata['requirements'] = self.requirements
        return metadata