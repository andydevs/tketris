"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from tkinter import *
from .mino import Mino

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

class Board(Frame):
    """
    Tketris Game Board
    """
    def __init__(self, master=None):
        """
        Initializes Game Board
        """
        super(Board, self).__init__(master)
        self.init_ui()
        self.bounds = Bounds()

        # Basic mino
        mino = Mino.random((0, 4))
        self.draw_tiles(mino.tiles, mino.color)

    def init_ui(self):
        """
        Initializes User Interface
        """
        self.tiles = []
        for i in range(20):
            row = []
            for j in range(10):
                tile = Canvas(self, width=20, height=20, bg='#ccc')
                tile.grid(row=i, column=j)
                row.append(tile)
            self.tiles.append(row)

    def draw_tile(self, tile, color):
        """
        Draws the given tile
        """
        if self.bounds.within_all_bounds(tile):
            self.tiles[tile[0]][tile[1]].config(bg=color)

    def draw_tiles(self, tiles, color):
        """
        Draws all tiles
        """
        for tile in tiles:
            self.draw_tile(tile, color)

    def clear_tiles(self):
        """
        Sets all tiles to clear color
        """
        for row in self.tiles:
            for tile in row:
                tile.config(bg='#ccc')
