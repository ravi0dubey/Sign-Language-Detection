# Setup file is created where we write statement so that signLanguage folder will behave as libraries
# This will install all folders as local package installation


from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e."


def get_requirements_list() -> List[str]:
    
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name = 'signLanguages',
    version= '0.0.0',
    author= 'Ravi Dubey',
    author_email= 'ravi0dubey@gmail.com',
    packages= find_packages(),
    install_requires = []

)