"""Tests for the grid module."""

import unittest

from grid import *

class TestPatch(unittest.TestCase):

    """Tests for the Patch class."""

    def test_patch_dimensions_are_consistent(self):
        """When constructing a Patch the input dimensions must be consistent."""
        with self.assertRaises(AssertionError):
            Patch((1,), (1., 2.))
