'''
    File name: setup.py
    Author: Henry Letton
    Date created: 2020-11-08
    Python Version: 3.8.3
    Description: Build script for setuptools.
        
'''

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-HennersMcGee",
    version="0.0.1",
    author="Henry Letton",
    author_email="henry_letton@hotmail.com",
    description="A package to store all personal functions in one place, for ease of use in many projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)