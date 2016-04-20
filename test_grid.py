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

import numpy as np

from grid import *

class TestPatchGrid(unittest.TestCase):

    """Tests for the PatchGrid class."""

    def setUp(self):
        """Registers a function to compare numpy ndarrays."""
        def compare_numpy_ndarrays(x, y, msg=None):
            if not (x == y).all():
                message = "Arrays are not equal ({} entries differ)" \
                    .format(np.count_nonzero(x - y))
                if msg is not None:
                    message += ", "+msg
                raise self.failureException(message)
        self.addTypeEqualityFunc(np.ndarray, compare_numpy_ndarrays)

    def test_patch_grid_has_positive_dimension(self):
        """A PatchGrid needs to have at least one dimension."""
        with self.assertRaises(AssertionError):
            PatchGrid((), (), ())

    def test_patch_grid_dimensions_are_consistent(self):
        """To construct a PatchGrid, consistent dimensions must be used."""
        with self.assertRaises(AssertionError):
            PatchGrid((1,), (1., 2.), (1., 2.))
        with self.assertRaises(AssertionError):
            PatchGrid((1, 2), (1., 2.), (1.,))

    def test_patch_grid_coordinates_returns_coordinates(self):
        """PatchGrid.coordinates should return the grid's coordinates."""
        patch_grid = PatchGrid((2, 2, 3), (3., 1., 2.), (2., 3., 5.))
        expected = np.array([[2., 2., 2., 2., 2., 2., 5., 5., 5., 5., 5., 5.],
                             [3., 3., 3., 4., 4., 4., 3., 3., 3., 4., 4., 4.],
                             [5., 7., 9., 5., 7., 9., 5., 7., 9., 5., 7., 9.]])
        self.assertEqual(patch_grid.coordinates(), expected)
