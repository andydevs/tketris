"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from ..numpy_algorithms import tileset_intersection, tile_in_set

"""
This file defines the code which checks for boundaries through which the
current mino is unable to move.

Before a mino is allowed to move, the action checks if the mino is occupying
the corresponding boundary. If so, it is not allowed to move in that direction
and will not respond to the command
"""

class Bound:
    """
    Generic bound class
    """
    def collision(self, tiles):
        """
        Check if any of the given tiles is within any of the tiles in the bound

        :param tiles: the tiles being checked

        :return: True if any of the given tiles is within any of the tiles
                 in the bound
        """
        return tileset_intersection(tiles, self.tiles)

class TileSetBound(Bound):
    """
    Bound for a side of a set of tiles
    """
    def __init__(self, root_tiles, axis, direction):
        """
        Initializes instance
        """
        self.root_tiles = root_tiles
        self.axis = axis
        self.direction = direction

    @property
    def normal(self):
        """
        Docstring for direction_vector property
        """
        norm = np.array([ 0, 0 ])
        norm[self.axis] = self.direction
        return norm

    @property
    def tiles(self):
        """
        The tiles that occupy this bound
        """
        if self.root_tiles.shape[0] == 0:
            return np.array([])
        else:
            bounds = self.root_tiles + self.normal
            bound_is_open = np.logical_not(tile_in_set(bounds, self.root_tiles))
            return np.compress(bound_is_open, bounds, axis=0)

class BoardBound(Bound):
    """
    Game board bound
    """
    def __init__(self, axis, endpoint, size):
        """
        Initializes instance
        """
        self.axis = axis
        self.endpoint = endpoint
        self.size = size

    @property
    def tiles(self):
        """
        The tiles that occupy this bound
        """
        tiles = []
        for i in range(self.size):
            tile = [i, i]
            tile[self.axis] = self.endpoint
            tiles.append(tile)
        return np.array(tiles)

class BoardBounds:
    """
    All Tketris game board bounds
    """
    def __init__(self):
        """
        Initializes bounds
        """
        self.left_bound = BoardBound(1, 0, 20)
        self.right_bound = BoardBound(1, 9, 20)
        self.down_bound = BoardBound(0, 19, 10)
