#!/usr/bin/env python

from setuptools import setup, Extension, find_packages
from pathlib import Path

import numpy
from Cython.Distutils import build_ext

project_root = Path(__file__).resolve().parent

with project_root.joinpath('requirements.txt').open('r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

with project_root.joinpath('readme.rst').open('r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension(
            'cprimes',
            sources=['cprimes.pyx'],
            include_dirs=[numpy.get_include()],
            # extra_compile_args=['/openmp'],
            # extra_link_args=['/openmp']
            # libraries=['m']
        )
    ],
    author='Doug Skrypa',
    author_email='dskrypa@gmail.com',
    description='Primes',
    long_description=long_description,
    url='https://github.com/dskrypa/primes',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    python_requires='~=3.4',
    install_requires=['wheel'] + requirements
)
