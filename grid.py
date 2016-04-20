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

"""Contains grid information.

Public classes:
    Patch
"""

__all__ = ['Patch']

import numpy as np

class Patch():

    """Represents a patch: a uniform grid section.

    Public methods:
        __init__

    Public attributes:
        dim - Number of dimensions of the patch.
        shape - Number of points along each dimension in the patch.
        spacing - Spacing between points along each dimension.
        first_point - Location of the point with the lowest coordinate values.
    """

    def __init__(self, shape, spacing, first_point):
        """Construct a Patch given numbers of points and grid spacings.

        Arguments (see class docstring for details):
            shape
            spacing
            first_point
        """
        self.dim = len(shape)
        self.size = np.prod(shape)
        assert self.dim > 0, "cannot construct a patch of dimension 0"
        assert self.dim == len(spacing) and self.dim == len(first_point), \
            "cannot construct a patch with arguments of inconsistent " \
            "dimensions ({}, {}, and {} are not all equal)"\
                .format(self.dim, len(spacing), len(first_point))
        self.shape = shape
        self.spacing = spacing
        self.first_point = first_point

    def coordinates(self):
        """Return the coordinates of all grid points.

        The output of this function is broadly similar to the output of
        numpy.meshgrid, except that instead of returning a series of vectors,
        this function returns a single two-dimensional array.

        As an example:

        >>> Patch((2, 3), (1., 1.), (0., 0.)).coordinates()
        array([[ 0.,  0.,  0.,  1.,  1.,  1.],
               [ 0.,  1.,  2.,  0.,  1.,  2.]])
        """
        coords = np.empty((self.dim, self.size))
        # Number of times a coordinate appears "in a row", and the number of
        # times we cycle through the coordinates.
        rep_num = self.size
        tile_num = 1
        for i in range(self.dim):
            rep_num //= self.shape[i]
            # The actual coordinate values, uniformly spaced points.
            coord_values = np.linspace(
                self.first_point[i],
                self.first_point[i] + (self.shape[i]-1)*self.spacing[i],
                self.shape[i],
            )
            coords[i,:] = np.tile(np.repeat(coord_values, rep_num), tile_num)
            tile_num *= self.shape[i]
        return coords
