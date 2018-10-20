"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

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
        self.score_label = Label(self, text="Score: 0")
        self.score_label.pack(fill=Y, expand=1)

    def display_score(self, score):
        """
        Docstring for add_score
        """
        self.score_label.config(text="Score: {}".format(score))
