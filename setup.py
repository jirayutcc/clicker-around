#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "clicker-around",
    description = ("clicker-around."),
    author = "Jirayutcc",
    version = "1.0.0",
    packages = ['src', 'tests', 'doc'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
    ],
)