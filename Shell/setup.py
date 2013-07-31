#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name = 'MyShell',
    version = '0.1',
    description = "Shell module.",
    long_description = "A test module for our book.",
    platforms = ["Linux"],
    py_modules=[
        'my_shell'
    ],
    license = "MIT",
    packages=find_packages()
    )
