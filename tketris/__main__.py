"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from . import Tketris
from tkinter import Tk

# Main code
if __name__ == '__main__':
    root = Tk()
    app = Tketris(root)
    app.pack()
    root.title('Tketris')
    root.resizable(False, False)
    root.mainloop()
