import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

INSTALL_REQUIRES = [
      'pandas'
]

setup(name="bmi_calculator",
      version=1.0,
      description="BMI Calculator allows in calculating BMI values along with category and risk factor",
      long_description="BMI Calculator allows in calculating BMI values along with category and risk factor",
      long_description_content_type="text/markdown",
      author="Rushikesh",
      author_email="rushikesh.meharwade@gmail.com",
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )