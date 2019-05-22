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

import pytest

import time

import foo
import version


class TestFoo():
    """Testing the Foo, and the version."""

    def test_version(self):
        """Test if the version if what we think it should be."""
        assert version.__version__ == version.get_version()

    def test_sleep(self):
        """Test if we can sleep and time out..."""
        print("pytest is hibernating for a little bit more than 5 minutes...")
        time.sleep(60 * 5 + 5)
        print("if running in a Pod, I got killed...")
