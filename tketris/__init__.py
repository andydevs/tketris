"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from .game import GameLogic
from .board import Board
from .side_menu import SideMenu
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
        self.start_game()

    def init_ui(self):
        """
        Initializes user interface
        """
        self.board = Board(self)
        self.board.pack(side=LEFT, fill=Y)
        self.side_menu = SideMenu(self)
        self.side_menu.pack(side=RIGHT, fill=Y)

    def init_events(self):
        """
        Docstring for init_events
        """
        self.master.bind('<Up>', self.handle_up)
        self.master.bind('<Left>', self.handle_left)
        self.master.bind('<Right>', self.handle_right)
        self.master.bind('<Down>', self.handle_down)

    def handle_up(self, event):
        """
        Docstring for handle_up
        """
        if self.game_continue:
            self.rotate()

    def handle_left(self, event):
        """
        Docstring for handle_down
        """
        if self.game_continue:
            self.move_left()

    def handle_right(self, event):
        """
        Docstring for handle_down
        """
        if self.game_continue:
            self.move_right()

    def handle_down(self, event):
        """
        Docstring for handle_down
        """
        if self.game_continue:
            self.move_down()

    def start_game(self):
        """
        Starts clock
        """
        self.side_menu.select_playing()
        self.game_continue = True
        self.run_clock()

    def run_clock(self):
        """
        Runs clock
        """
        if self.game_continue:
            self.clock_tick_update()
            self.master.after(1000, self.run_clock)

    def game_over_event(self):
        """
        Docstring for game_over_event
        """
        self.side_menu.select_game_over()
