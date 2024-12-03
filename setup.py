import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
Repo_name = "chicken-disease-classification"
Author_user_name = "muhammed_usman"
SRC_Repo = "cnnClassifier"
Author_email = "uthmanuthaimin01@gmail.com"

setuptools.setup(
    name=SRC_Repo,
    version=__version__,
    author=Author_user_name,
    author_email=Author_email,
    description="A simple python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_user_name}/{Repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_user_name}/{Repo_name}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

