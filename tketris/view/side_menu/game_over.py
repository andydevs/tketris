"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

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
