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
 - Patch
"""

__all__ = ['Patch']

class Patch():

    """Represents a patch: a uniform grid section.

    Public methods:
    __init__
    """

    def __init__(self, num_points, spacings, first_point):
        """Construct a Patch given numbers of points and grid spacings.

        Arguments:
            num_points - Number of points in the patch, along each dimension.
            spacings - Spacing between points, along each dimension.
            first_point - Coordinates of the first point (the corner of the
                patch with the lowest coordinate in each dimension).
        """
        self.dim = len(num_points)
        assert self.dim == len(spacings) and self.dim == len(first_point), \
            "cannot construct a patch with arguments of inconsistent " \
            "dimensions ({}, {}, and {} are not all equal)"\
                .format(self.dim, len(spacings), len(first_point))
        self.num_points = num_points
        self.spacings = spacings
        self.first_point = first_point
