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
        self.init_events()
        self.run_clock()

    def init_ui(self):
        """
        Initializes user interface
        """
        self.board = Board()
        self.board.pack()

    def init_events(self):
        """
        Docstring for init_events
        """
        self.master.bind('<Left>', self.board.move_left)
        self.master.bind('<Right>', self.board.move_right)
        self.master.bind('<Down>', self.board.move_down)

    def run_clock(self):
        """
        Runs clock
        """
        print('Clock ticked!')
        self.after(1000, self.run_clock)
