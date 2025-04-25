from readme_gen.parser.github_parser import GitHubParser
from readme_gen.generator.content_formatter import ContentFormatter
from readme_gen.collector.data_reader import DataReader
from readme_gen.logger import logging

if __name__=='__main__':
    try:
        logging.info('Starting the application...')

        # # Code to parse a GitHub repository
        # repo_url = input("Enter the GitHub repository URL: ")
        # gp = GitHubParser()
        # print(gp.parse_repo(repo_url))

        # Code to 

        static_metadata = {'project_name': 'REAME', 'files': ['app.py', 'LICENSE', 'README.md', 'requirements.txt', 'setup.py', 'template.py', 'readme_gen\\exception.py', 'readme_gen\\logger.py', 'readme_gen\\utils.py', 'readme_gen\\__init__.py', 'readme_gen\\collector\\data_reader.py', 'readme_gen\\collector\\__init__.py', 'readme_gen\\generator\\content_formatter.py', 'readme_gen\\generator\\content_writer.py', 'readme_gen\\generator\\__init__.py', 'readme_gen\\parser\\github_parser.py', 'readme_gen\\parser\\local_parser.py', 'readme_gen\\parser\\__init__.py', 'readme_gen\\templates\\default.md.jinja', 'readme_gen\\templates\\__init__.py', 'readme_gen\\temp_project_directory\\project_requirements.txt', 'readme_gen\\temp_project_directory\\project_structure.txt', 'readme_gen\\tests\\test_github_parser.py', 'readme_gen\\tests\\test_local_parser.py', 'readme_gen\\tests\\__init__.py'], 'directories': ['readme_gen', 'readme_gen\\collector', 'readme_gen\\generator', 'readme_gen\\parser', 'readme_gen\\templates', 'readme_gen\\temp_project_directory', 'readme_gen\\tests'], 'has_readme': True, 'has_license': True, 'has_requirements': True, 'languages': ['.py', '.md', '.jinja', '.txt']}



        # generate a README file
        # cf = ContentFormatter()
        # generated_readme = cf.generate_readme(static_metadata)


        # Reading data 
        dr = DataReader()
        dr.requirement_collector(static_metadata)

        # with open("genREADME.md", "w", encoding="utf-8") as file:
        #     file.write(generated_readme)
        logging.info('README file has been generated and saved as genREADME.md.')

        logging.info('Application finished successfully.')
    except Exception as e:
        logging.error(f"An error occurred: {e}")