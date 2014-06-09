#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from superpaste import __version__ as version

setup(
    name='superpaste',
    version=version,
    description='Upgrade to standard unix paste command',
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    url='https://github.com/lmaurits/superpaste',
    license="BSD (3 clause)",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
    py_modules = ['superpaste',],
    scripts = ['bin/superpaste',],

)
