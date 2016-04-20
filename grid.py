"""Contains grid information.
"""

class Patch():

    """Represents a patch: a uniform grid section.

    Public methods:
    __init__
    """

    def __init__(self, num_points, spacings):
        """Construct a Patch given numbers of points and grid spacings.

        Arguments:
            num_points - Number of points in the patch, along each dimension.
            spacings - Spacing between points, along each dimension.
        """
        assert len(num_points) == len(spacings), \
            "cannot construct a patch with num_points and spacings of " \
            "different length ({} != {})".format(len(num_points), len(spacings))
        self.num_points = num_points
        self.spacings = spacings
