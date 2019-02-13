"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

class PlayingMenu(Frame):
    """
    The side menu shown during gameplay.
    """
    def __init__(self, master=None):
        """
        Initializes Frame
        """
        super(PlayingMenu, self).__init__(master)
        self.init_ui()

    def init_ui(self):
        """
        Initializes UI
        """
        self.score = Label(self, text="Score: 0")
        self.score.pack(fill=Y, expand=1)

        # Buttons frame
        self.buttons = Frame(self)
        self.pause = Button(self.buttons,
            text="Pause",
            command=self.toggle_game_resume)
        self.pause.pack()
        self.buttons.pack(fill=Y, expand=1)

    def display_score(self, score):
        """
        Display current score
        
        :param score: the current score to display
        """
        self.score.config(text="Score: {}".format(score))

    def display_game_resume_state(self, resume):
        """
        Display the appropriate pause/resume button text
        based on resume state
        
        :param resume: true if the game has resumed, false if paused
        """
        if resume:
            self.pause.config(text="Pause")
        else:
            self.pause.config(text="Resume")

    def toggle_game_resume(self):
        """
        Toggle game pause or resume
        """
        self.master.toggle_game_resume()
