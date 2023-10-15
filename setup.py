import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"
REPO_NAME = "NLP_textsummary"
AUTHOR_NAME = "Amit Kumar"
SRC_REPO = "NLP_textsummary"
AUTHOR_EMAIL = "amitprataprana41@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=f"A python package for Text Summarization NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amitkumar41/NLP_textsummary",
    project_urls={
        "Bug Tracker": f"https://github.com/amitkumar41/NLP_textsummary/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)