"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np

class BoardBound:
    """
    Tketris bound for a side of the game board
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
            check=np.greater if self.positive else np.less,
            combine=np.any,
            tiles=tiles)

class BoardBounds:
    """
    All Tketris game board bounds
    """
    def __init__(self):
        """
        Initializes bounds
        """
        self.left_bound = BoardBound(1, 0, False)
        self.right_bound = BoardBound(1, 9, True)
        self.up_bound = BoardBound(0, 0, False)
        self.down_bound = BoardBound(0, 19, True)

    def within_all_bounds(self, tiles):
        """
        True if the tiles are within all bounds
        """
        return self.left_bound.is_within(tiles) \
            and self.right_bound.is_within(tiles) \
            and self.up_bound.is_within(tiles) \
            and self.down_bound.is_within(tiles)

class TileSetBound:
    """
    Bound for a side of a set of tiles
    """
    def __init__(self, root_tiles, direction):
        """
        Initializes instance
        """
        self.root_tiles = root_tiles
        self.direction = direction

    @property
    def tiles(self):
        """
        Docstring for bound property
        """
        individual_boundaries = self.root_tiles + self.direction
        return np.array([
            boundary for boundary in individual_boundaries
            if not any(np.all(np.equal(tile, boundary)) for tile in self.root_tiles)
        ])
