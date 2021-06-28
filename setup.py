#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
txt2pdf - setup file
"""

from os import path

import txt2pdf

from setuptools import setup, find_packages

# Read README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(requirements, ignore=("setuptools",)):
    """
    Read dependencies from requirements file (with version numbers if any)

    Notes:
        - this implementation does not support requirements files with extra
          requirements
        - this implementation has been taken from TailorDev/Watson's setup file
    """
    with open(requirements) as f:
        packages = set()
        for line in f:
            line = line.strip()
            if line.startswith(("#", "-r", "--")):
                continue
            if "#egg=" in line:
                line = line.split("#egg=")[1]
            pkg = line.strip()
            if pkg not in ignore:
                packages.add(pkg)
        return list(packages)


setup(
    name="txt2pdf",
    version=txt2pdf.__version__,
    packages=find_packages(),
    scripts=[
        "scripts/txt2pdf",
    ],
    install_requires=parse_requirements("requirements.txt"),
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=parse_requirements("requirements-dev.txt"),
    url="https://github.com/c4ffein/txt2pdf",
    author="Julien Maupetit & c4ffein",
    author_email="c4ffein@gmail.com",
    description="txt2pdf, a Markdown to PDF conversion tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords="markdown converter css pdf",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Customer Service",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Office/Business",
        "Topic :: Utilities",
    ],
)
