"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from . import Tketris

# Main code
if __name__ == '__main__':
    app = Tketris()
    app.master.title('Tketris')
    app.master.resizable(False, False)
    app.mainloop()
