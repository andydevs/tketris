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

    def __init__(self, master=None):
        """
        Initializes master
        """
        super(SideMenu, self).__init__(master, bd=1, bg=self.side_menu_color)
        self.init_ui()

    def init_ui(self):
        """
        Initializes ui
        """
        self.label = Label(self, text="SideMenu")
        self.label.pack(fill=Y, expand=1)
