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
        # Game over label
        self.game_over_label = Label(self, text="Game Over")
        self.game_over_label.pack(fill=Y, expand=1)
        self.final_score_label = Label(self, text="Final Score: 0")
        self.final_score_label.pack(fill=Y, expand=1)

        # Buttons frame
        self.buttons = Frame(self)
        self.reset_button = Button(self.buttons,
            text="Restart",
            command=self.reset_game)
        self.reset_button.pack()
        self.buttons.pack(fill=Y, expand=1)

    def display_final_score(self, final_score):
        """
        Docstring for display_final_score
        """
        self.final_score_label.config(text="Final Score: {}".format(final_score))

    def reset_game(self):
        """
        Docstring for reset_game
        """
        self.master.reset_game()
