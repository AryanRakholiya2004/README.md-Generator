from readme_gen.parser.github_parser import GitHubParser
from readme_gen.logger import logging

if __name__=='__main__':
    try:
        logging.info('Starting the application...')
        repo_url = input("Enter the GitHub repository URL: ")
        gp = GitHubParser()
        print(gp.parse_repo(repo_url))
    except Exception as e:
        logging.error(f"An error occurred: {e}")