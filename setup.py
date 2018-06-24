#!/usr/bin/python3

import os
from setuptools import setup


setup(
    name='thoth-srcops-testing',
    version='0.1.0-rc.1',
    zip_safe=False,
    author='Christoph Görn',
    author_email='goern@redhat.com',
    maintainer='Christoph Görn',
    maintainer_email='goern@redhat.com',
    description='This is a test.',
    py_modules=['food'],
    url='https://github.com/thoth-station/srcops-testing',
    license='GPLv3+',
    keywords='srcops thoth zuul',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License:: OSI Approved:: GNU General Public License v3 or later(GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
