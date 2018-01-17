#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
]


def get_version():
    init = open(os.path.join(ROOT, 'python_dash', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='python_dash',
    version=get_version(),
    description='A wrapper for the Dash CLI in Python',
    long_description='A wrapper for the Dash CLI in Python',
    author='James Bowen',
    url='https://github.com/JamesDBowen/python_dash',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    license="MIT",
    classifiers=[
        'Development Status :: 1 - Planning Development Status',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
