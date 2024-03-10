from setuptools import find_packages,setup

hyphen_e="-e ."


def get_requirements(file_path):  #: this tell that it accept a path of type str and return a list of str items:
  with open(file_path,'r') as f:
    requirements=[]
    requirements=f.readlines()
    requirements=[item.replace("\n","") for item in requirements]
    
    if hyphen_e in requirements:
      requirements.remove(hyphen_e)
    
    return requirements




#" this is the meta data about my project
setup(
  name="mlproject",
  version="0.0.1",
  author="magnum",
  author_email='ankitsrivastav2202@gmail.com',
  packages=find_packages(),   
  #: this will find the packages that will be required,
  #: if we want to find src as a package so that we can import it anywhere in the program , we wil create a file __init__.py,
  #: now when find packages go and find __init__.py and that folder will be able to used as package and import any where in the program
  install_requires=get_requirements('requirements.txt')
  )