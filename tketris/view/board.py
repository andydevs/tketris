"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *
import numpy as np

class Board(Frame):
    """
    Tketris Game Board where the mino magic happens!
    """
    bg_color = "white"
    clear_color = None
    box_size = 20

    def __init__(self, master=None):
        """
        Initializes Game Board
        """
        super(Board, self).__init__(master, bg=self.bg_color)
        self.init_ui()

    def init_ui(self):
        """
        Initializes User Interface
        """
        # Set color to background if color is not given
        if self.clear_color is None:
            self.clear_color = self.master['bg']

        # Set tiles
        self.tiles = []
        for i in range(20):
            row = []
            for j in range(10):
                tile = Canvas(self,
                    width=self.box_size,
                    height=self.box_size,
                    bg=self.clear_color)
                tile.grid(row=i, column=j)
                row.append(tile)
            self.tiles.append(row)

    def draw_tile(self, tile, color):
        """
        Draws the given tile
        """
        if 0 <= tile[0] and tile[0] <= 19 and 0 <= tile[1] and tile[1] <= 9:
            self.tiles[tile[0]][tile[1]].config(bg=color)

    def draw_tiles(self, tiles, color):
        """
        Draws all tiles
        """
        for tile in tiles.tolist():
            self.draw_tile(tile, color)

    def clear_tiles(self):
        """
        Sets all tiles to clear color
        """
        for row in self.tiles:
            for tile in row:
                tile.config(bg=self.clear_color)
