from setuptools import setup, find_packages
from typing import List

HYPEN_E_DASH = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DASH in requirements:
            requirements.remove(HYPEN_E_DASH)
    return requirements

setup(
    name="src",
    version='0.0.1',
    author="Damodar",
    author_email='damodarryadav@gmail.com',
    description=('Sensor fault predication using machine learning.'),
    packages=find_packages(),
    install_requires=[],
)