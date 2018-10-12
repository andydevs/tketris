"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *
from .game import GameLogic

class Board(Frame, GameLogic):
    """
    Tketris Game Board
    """
    def __init__(self, master=None):
        """
        Initializes Game Board
        """
        super(Board, self).__init__(master)
        self.init_ui()
        self.init_game()

        # Start game
        self.new_mino()

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
        if 0 <= tile[0] and tile[0] <= 19 and 0 <= tile[1] and tile[1] <= 9:
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
