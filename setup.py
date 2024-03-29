# Upload package to PyPi.

from setuptools import setup

setup(name='yalelaundry',
      version='0.3.0',
      description='Library for fetching data from the Yale Laundry APIs.',
      url='https://github.com/ErikBoesen/yalelaundry',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['yalelaundry'],
      install_requires=['requests'])
