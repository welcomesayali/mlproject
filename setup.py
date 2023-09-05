## google search "python setup.py" --will be responsible for creating my ML application as a package and even deploy in PyPI.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
   
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # reads from that file one by one
        requirements=[req.replace("\n","") for req in requirements] # we get "\n" otherwise therefore we replace \n by blank


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


## metadata info about the entire project
setup( 
name='mlproject',
version='0.0.1',
author='sayali',
author_email='patilsayali2@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)