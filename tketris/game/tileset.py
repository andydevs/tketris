"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import TileSetBound

class TileSet:
    """
    Represents a unitary set of tiles in Tketris
    """
    @property
    def left_bound(self):
        """
        Left boundary of tileset
        """
        return TileSetBound(self.tiles, 1, -1)

    @property
    def right_bound(self):
        """
        Right boundary of tileset
        """
        return TileSetBound(self.tiles, 1, 1)

    @property
    def up_bound(self):
        """
        Upper boundary of tileset
        """
        return TileSetBound(self.tiles, 0, -1)

    @property
    def down_bound(self):
        """
        Lower boundary of tileset
        """
        return TileSetBound(self.tiles, 0, 1)

class BoardTileSet(TileSet):
    """
    Current tiles on the board
    """
    def __init__(self, tile_colors=[]):
        """
        Initializes instance
        """
        self.tile_colors = tile_colors

    @property
    def tiles(self):
        """
        Docstring for tiles property
        """
        return np.array([[i, j] for i, j, color in self.tile_colors])
