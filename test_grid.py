# Copyright 2016 Sean Patrick Santos
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for the grid module."""

import unittest

from grid import *

class TestPatch(unittest.TestCase):

    """Tests for the Patch class."""

    def test_patch_dimensions_are_consistent(self):
        """When constructing a Patch the input dimensions must be consistent."""
        with self.assertRaises(AssertionError):
            Patch((1,), (1., 2.), (1., 2.))
        with self.assertRaises(AssertionError):
            Patch((1, 2), (1., 2.), (1.,))
