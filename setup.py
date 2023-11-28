from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requirements
    reqruirements=[]
    with open(file_path) as file_obj:
        reqruirements = file_obj.readlines()
        reqruirements = [req.replace('\n','') for req in reqruirements]

        if HYPHEN_E_DOT in reqruirements:
            reqruirements.remove(HYPHEN_E_DOT)

    return reqruirements


setup(
    name='Laptop Price Prediction',
    version='0.0.1',
    author='mahbub',
    author_email='mahbubhossain249@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)