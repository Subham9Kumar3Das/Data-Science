from setuptools import find_packages,setup
from typing import List

hypen='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path,'r') as file:
        requirements=file.readlines() 
        requirements=[i.replace('\n','') for i in requirements]

        if hypen in requirements:
            requirements.remove(hypen)

        return requirements


setup(
    name='Diamond_Price_Prediction',
    version='0.0.1',
    author='Subham',
    author_email='subhamkumard67@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)