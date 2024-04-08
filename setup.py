from setuptools import find_packages,setup
from typing import List # type:ignore

HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will the list of string
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
        

setup(
    name="Mlproject",
    version="0.0.1",
    author="Alok sharma",
    author_email="aloksharma355450@gmail.com",
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
    
)