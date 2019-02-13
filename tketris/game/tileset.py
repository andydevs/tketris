"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import TileSetBound

class BoardTileSet:
    """
    Represents all tiles currently on the board.
    Handles boundaries for tiles and row completion detection.
    """
    def __init__(self, tile_colors=[]):
        """
        Initializes instance with the given initial tile colors
        
        :param tile_colors: initial tile_colors
        """
        self.tile_colors = tile_colors

    def clear_tiles(self):
        """
        Clears all tiles from board
        """
        self.tile_colors = []

    def add_tiles(self, tiles, color):
        """
        Adds the given tiles in the given color to the tileset
        
        :param tiles: set of tiles to add
        :param color: color of new tiles being added
        """
        for tile in tiles.tolist():
            self.tile_colors.append((tile[0], tile[1], color))

    def clear_rows(self):
        """
        Clears all full rows.
        
        :return: number of rows cleared
        """
        cleared_rows = 0
        required_columns = {i for i in range(10)}
        rows = {tile[0] for tile in self.tile_colors}
        for row in rows:
            # Check if all required columns are in row
            columns = {tile[1] for tile in self.tile_colors if tile[0] == row}
            clear_row = all(required in columns for required in required_columns)
            if clear_row:
                self.tile_colors = [
                    (i + 1 if i < row else i, j, color)
                    for i, j, color in self.tile_colors if i != row
                ]
                cleared_rows += 1
        return cleared_rows

    @property
    def tiles(self):
        """
        All tiles in the tileset as a numpy tileset
        """
        return np.array([[i, j] for i, j, color in self.tile_colors])

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
