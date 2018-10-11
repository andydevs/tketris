"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from .board import Board
from tkinter import *

class Tketris(Frame):
    """
    Tketris application instance
    """
    def __init__(self, master=None):
        """
        Initializes application instance
        """
        super(Tketris, self).__init__(master)
        self.init_ui()

    def init_ui(self):
        """
        Initializes user interface
        """
        self.board = Board()
        self.board.pack()
