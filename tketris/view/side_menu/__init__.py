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
    Side Menu Frame which displays game state and score
    Handles actions like pause/resume and restart and
    switching between playing and game over menus
    """
    side_menu_color = "#ccc"
    current_menu = None

    def __init__(self, master=None):
        """
        Initializes Frame
        """
        super(SideMenu, self).__init__(master,
            bd=1,
            bg=self.side_menu_color,
            width=20)
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI
        """
        self.select_playing()

    def select_menu(self, MenuType):
        """
        Select new menu to display
        """
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = MenuType(self)
        self.current_menu.pack(fill=Y, expand=1, ipadx=10, ipady=10)

    def select_game_over(self):
        """
        Display game over menu
        """
        self.select_menu(GameOverMenu)

    def select_playing(self):
        """
        Display select playing menu
        """
        self.select_menu(PlayingMenu)

    def display_score(self, score):
        """
        Display current score
        
        :param score: current score of game
        """
        if type(self.current_menu) is PlayingMenu:
            self.current_menu.display_score(score)

    def display_game_resume_state(self, resume):
        """
        Display game resume state
        
        :param resume: true if game is resumed, false if paused
        """
        if type(self.current_menu) is PlayingMenu:
            self.current_menu.display_game_resume_state(resume)

    def display_final_score(self, final_score):
        """
        Display final game score
        
        :param final_score: final score of the game
        """
        if type(self.current_menu) is GameOverMenu:
            self.current_menu.display_final_score(final_score)

    def reset_game(self):
        """
        Handle for starting new game
        """
        self.master.reset_game()

    def toggle_game_resume(self):
        """
        Handle for toggle game resume
        """
        self.master.toggle_game_resume()
