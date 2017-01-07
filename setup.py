#/usr/bin/env python
# coding:utf-8
# author: andy zhou
# date: 2016.11.7

import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(here, 'README.md')
changes_file = os.path.join(here, 'CHANGES.md')

def read_text(file_path):
    """
    fix the default operating system encoding is not utf8.
    """
    if sys.version_info.major < 3:
        with open(file_path) as f:
            return f.read()
    with open(file_path, encoding="utf8") as f:
        return f.read()

README = read_text(os.path.join(here, 'README.md'))
CHANGES = read_text(os.path.join(here, 'CHANGES.txt'))

requires = [
    'setuptools>=1.0',
]

test_requirements = [
    'nose',
]


setup(

    name='ailearn',
    description='machine learning algorithms',
    version='0.0.1',
    author='andy zhou',
    author_email='ablo_zhou@163.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=README + '\n\n' + CHANGES,
    url='https://github.com/ablozhou/ailearn',
    install_requires=requires,
    tests_require=test_requirements,
    platforms='all platform',
    license='Apache License 2.0',
)
