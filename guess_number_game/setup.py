#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:09:59 2020

@author: sasaki
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='guess_number_game',
                 version='0.0.1',
                 description='Guess the number game.',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author='Karin Sasaki',
                 author_email="karinsasaki@gmail.com",
                 url="",
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent"],
                 python_requires='>=3.6',
                 )
