"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

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

    def reset_game(self):
        """
        Docstring for reset_game
        """
        self.master.handle_reset_game()

class PlayingMenu(Frame):
    """
    Shows the PlayingMenu
    """
    def __init__(self, master=None):
        """
        Initializes instance
        """
        super(PlayingMenu, self).__init__(master)
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI
        """
        self.label = Label(self, text="Playing")
        self.label.pack(fill=Y, expand=1)

class GameOverMenu(Frame):
    """
    Shows the GameOver Menu
    """
    def __init__(self, master=None):
        """
        Initializes instance
        """
        super(GameOverMenu, self).__init__(master)
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI
        """
        self.label = Label(self, text="Game Over")
        self.label.pack()
        self.reset_button = Button(self, text="Restart", command=self.reset_game)
        self.reset_button.pack()

    def reset_game(self):
        """
        Docstring for reset_game
        """
        self.master.reset_game()
