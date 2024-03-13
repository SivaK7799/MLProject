from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

g = get_requirements(r'D:\NEW_ML_PJCT\requirements.txt')    

setup(
    name = 'NEW_ML_PJCT',
    version ='0.0.1',
    author = 'SPIDY',
    author_email = 'siva.k107799@gmail.com',
    install_requires = g,
    packages=find_packages()
)