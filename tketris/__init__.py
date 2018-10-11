"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from tkinter import *

class Tketris(Frame):
    """
    Tketris application instance
    """
    def __init__(self, master=None):
        """
        Initializes application instance
        """
        super(Tketris, self).__init__(master)
