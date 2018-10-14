"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from .game import GameLogic
from .board import Board
from tkinter import *

class Tketris(Frame, GameLogic):
    """
    Tketris application instance
    """
    DEBUG = False

    def __init__(self, master=None):
        """
        Initializes application instance
        """
        super(Tketris, self).__init__(master)
        self.init_ui()
        self.init_events()
        self.init_game()
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
        self.master.bind('<Up>', self.rotate)
        self.master.bind('<Left>', self.move_left)
        self.master.bind('<Right>', self.move_right)
        self.master.bind('<Down>', self.move_down)

    def run_clock(self):
        """
        Runs clock
        """
        self.clock_tick_update()
        self.master.after(1000, self.run_clock)
