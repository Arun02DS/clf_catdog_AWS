from setuptools import setup,find_packages
from typing import List
"""
The setup script is the center of all activity in building, 
distributing, and installing modules using the setuptools. 

"""

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """
    Description: This fucntion read all required packages for project.

    Return: List of requirement.txt

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list




setup(
    name="cat_dog_clf",
    version="0.0.1",
    author="Arun02DS",
    author_email="arun02negime@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)