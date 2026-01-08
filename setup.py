from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # This function reads the requirements from a given file and returns them as a list
    requirements =[]
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

     


setup(   
    name='mlproject',
    version='0.0.1',
    author='Miyuni',
    author_email='miyunilowe5@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)