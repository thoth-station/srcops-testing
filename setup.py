#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# thoth-package-extract
# Copyright(C) 2018,2019 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A foo module for SrcOps-testing."""


import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


with open('README.md') as fh:
    long_description = fh.read()


def get_version():
    with open('version.py') as f:
        content = f.readlines()

    for line in content:
        if line.startswith('__version__ ='):
            return line.split(' = ')[1][1:-2]
    raise ValueError("No version identifier found")

class Test(TestCommand):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass into py.test")
    ]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = ['--timeout=360', '--cov=.', '--capture=no', '--verbose']

    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.pytest_args))

setup(
    name='thoth-srcops-testing',
    version=get_version(),
    zip_safe=False,
    author='Christoph Görn',
    author_email='goern@redhat.com',
    maintainer='Christoph Görn',
    maintainer_email='goern@redhat.com',
    description='This is a test.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['foo'],
    tests_require=["pytest","pytest-cov","pytest-timeout"],
    cmdclass={'test': Test},
    url='https://github.com/thoth-station/srcops-testing',
    license='GPLv3+',
    keywords='srcops thoth zuul',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
