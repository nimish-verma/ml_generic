from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''this function will return the list of requirments'''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        # requirements = [req.replace ("\n") for req in requirements] #wrong syntax
        requirements = [req.replace("\n", "") for req in requirements]

        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
        
    
    
    
setup(
    name = "mlproject",
    version = '0.0.1',
    author ='nim',
    author_email = 'vnimish20@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn'],
    
    install_requires = get_requirements('requirements.txt')
)