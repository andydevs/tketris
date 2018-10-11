"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

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
