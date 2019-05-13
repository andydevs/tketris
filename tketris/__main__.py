"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from . import Tketris
from tkinter import Tk
from argparse import ArgumentParser
from sys import argv

# Argument Parser
parser = ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true')

# Main code
if __name__ == '__main__':
    args = parser.parse_args(argv[1:])
    root = Tk()
    app = Tketris(root, debug=args.debug)
    app.pack()
    root.title('Tketris')
    root.resizable(False, False)
    root.mainloop()
