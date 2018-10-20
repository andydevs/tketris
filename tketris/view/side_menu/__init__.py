"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *
from .game_over import GameOverMenu
from .playing import PlayingMenu

class SideMenu(Frame):
    """
    Side Menu Frame
    """
    side_menu_color = "#ccc"
    current_menu = None

    def __init__(self, master=None):
        """
        Initializes master
        """
        super(SideMenu, self).__init__(master, bd=1, bg=self.side_menu_color)
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI
        """
        self.select_playing()

    def select_menu(self, MenuType):
        """
        Select new menu
        """
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = MenuType(self)
        self.current_menu.pack(fill=BOTH, expand=1)

    def select_game_over(self):
        """
        Docstring for select_game_over
        """
        self.select_menu(GameOverMenu)

    def select_playing(self):
        """
        Docstring for select_playing
        """
        self.select_menu(PlayingMenu)

    def display_score(self, score):
        """
        Docstring for display_score
        """
        if type(self.current_menu) is PlayingMenu:
            self.current_menu.display_score(score)

    def reset_game(self):
        """
        Docstring for reset_game
        """
        self.master.reset_game()
