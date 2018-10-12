"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np

class Bound:
    """
    Tketris side bound
    """
    def __init__(self, index, endpoint, positive):
        """
        Initialize side bound

        :param index: the index to check
        :param endpoint: the endpoint value of the bound
        :param positive: true if the value has to be less than the endpoint
        """
        self.index = index
        self.endpoint = endpoint
        self.positive = positive

    def _check_bound(self, check, combine, tiles):
        """
        Generic boundary checker for the given tiles
        """
        if len(tiles.shape) == 1:
            return check(tiles[self.index], self.endpoint)
        else:
            return combine(check(tiles[:, self.index], self.endpoint))

    def is_within(self, tiles):
        """
        True if all tiles are within the bound
        """
        return self._check_bound(
            check=np.less_equal if self.positive else np.greater_equal,
            combine=np.all,
            tiles=tiles)

    def is_outside(self, tiles):
        """
        True if any tiles are outside the bound
        """
        return self._check_bound(
            check=np.greater_equal if self.positive else np.less_equal,
            combine=np.any,
            tiles=tiles)

class Bounds:
    """
    Tketris game bounds
    """
    def __init__(self):
        """
        Initializes bounds
        """
        self.left_bound = Bound(1, 0, False)
        self.right_bound = Bound(1, 9, True)
        self.up_bound = Bound(0, 0, False)
        self.down_bound = Bound(0, 19, True)

    def within_all_bounds(self, tiles):
        """
        True if the tiles are within all bounds
        """
        return self.left_bound.is_within(tiles) \
            and self.right_bound.is_within(tiles) \
            and self.up_bound.is_within(tiles) \
            and self.down_bound.is_within(tiles)
