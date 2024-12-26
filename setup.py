from setuptools import find_packages,setup 
from typing import List 
HYPHEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
     '''
     this function will return the list of requirements 
     
     '''
     requirements=[]
     with open (file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
            
     return requirements        
         
         
         
setup(
    name='mlproject',
    version='0.0.1',
    author='Nilaya',
    author_email='nilayahuddar@gmail.com',
    packages=find_packages(),
    #install requires actually takes a list with all the required packages , sometimes specifying all packages in the list is not feasible 
    
    install_requires=get_requirements('requirements.txt'),
)