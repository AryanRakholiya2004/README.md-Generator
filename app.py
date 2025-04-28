import streamlit as st
from readme_gen.parser.github_parser import GitHubParser
from readme_gen.generator.content_formatter import ContentFormatter
from readme_gen.generator.content_writer import ContentWriter
from readme_gen.collector.data_reader import DataReader
from readme_gen.logger import logging
import os

# Streamlit app
st.title("README.md Generator")

# Input fields
st.sidebar.header("Input Parameters")
api_key = st.sidebar.text_input("Gemini API Key", type="password",value='AIzaSyA2AcQKRByAmWBflY-1kwU29qcibr71QJI')
repo_url = st.sidebar.text_input("GitHub Repository URL",value='https://github.com/AryanRakholiya2004/Bank-customer-churn-end-to-end-project')


if st.sidebar.button("Generate README"):
    if not api_key or not repo_url:
        st.error("Both API key and GitHub repository URL are required.")
    else:
        try:
            logging.info('Starting the README generation process...')

            gp = GitHubParser()
            metadata = gp.parse_repo(repo_url)
            
            # Reading data
            dr = DataReader()
            metadata = dr.requirement_collector(metadata)

            # Writing requirements to a file
            cr = ContentWriter()
            cr.save_requirement_txt(metadata['requirements'])
            cr.project_description_write(metadata, api_key)

            # Generate a README file
            cf = ContentFormatter()
            generated_readme = cf.generate_readme(metadata)

            # Save the README file
            output_file = "Generated_README.md"
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(generated_readme)

            logging.info('README file has been generated and saved as genREADME.md.')

            # Display the generated README content
            st.success("README.md has been generated successfully!")
            # Add tabs for Markdown preview and code
            tab1, tab2 = st.tabs(["Markdown Preview", "Markdown Code"])

            # Markdown Preview tab
            with tab1:
                st.markdown(generated_readme, unsafe_allow_html=True)

            # Markdown Code tab
            with tab2:
                st.text_area("Generated README.md", generated_readme, height=400)

            # Provide a download link
            with open(output_file, "rb") as file:
                btn = st.download_button(
                    label="Download README.md",
                    data=file,
                    file_name=output_file,
                    mime="text/markdown"
                )

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            st.error(f"An error occurred: {e}")
