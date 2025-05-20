from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Movie Recommender System"
AUTHOR_USER_NAME = "Mausham Kumar"
SRC_REPO = "Movie_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Mausham Kumar",
    description="A small local packages for ML based Movie recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maushamkumar/Recommender-System/tree/main/End%20to%20End%20Book%20Recommendation",
    author_email="Maushamkumarr26@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)