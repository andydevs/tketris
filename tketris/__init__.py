"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from .game import GameLogic
from .view.board import Board
from .view.side_menu import SideMenu
from tkinter import *

class Tketris(Frame, GameLogic):
    """
    The main application frame. Includes the GameLogic mixin
    """
    DEBUG = False

    def __init__(self, master=None, debug=False):
        """
        Initializes application instance
        """
        super(Tketris, self).__init__(master)
        self.DEBUG = debug
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
        Initializes keybound events
        """
        self.master.bind('<Up>', self.rotate)
        self.master.bind('<Left>', self.move_left)
        self.master.bind('<Right>', self.move_right)
        self.master.bind('<Down>', self.move_down)

    def reset_game(self):
        """
        Resets game
        """
        if not self.game_continue:
            self.start_game()

    def toggle_game_resume(self):
        """
        Toggle game resume state and update menu
        """
        self.game_resume = not self.game_resume
        self.side_menu.display_game_resume_state(self.game_resume)

    def run_clock(self):
        """
        Runs clock
        """
        if self.game_continue:
            if self.game_resume:
                self.clock_tick_update()
            self.master.after(1000, self.run_clock)

    def on_start_game(self):
        """
        Select playing and start clock on start game
        """
        self.side_menu.select_playing()
        self.run_clock()

    def on_game_over(self):
        """
        Displays game over menu and display final score on game over
        """
        self.side_menu.select_game_over()
        self.side_menu.display_final_score(self.score)

    def on_update_score(self):
        """
        Display score on playing menu on update score
        """
        self.side_menu.display_score(self.score)
