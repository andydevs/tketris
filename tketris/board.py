"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from tkinter import *
from .mino import Mino

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
        mino = Mino.random((5, 4))
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

    def within_bounds(self, tile):
        """
        True if the given tile posisiton is within bounds
        """
        return np.all(
            np.logical_and(
                np.greater_equal(tile, [0, 0]),
                np.less_equal(tile, [19, 9])
            )
        )

    def draw_tile(self, tile, color):
        """
        Draws the given tile
        """
        if self.within_bounds(tile):
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
