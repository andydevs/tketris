"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import Bounds
from .mino import Mino, IMino, JMino

class GameLogic:
    """
    Tketris Game Logic mixin
    """
    def init_game(self):
        """
        Initialize game
        """
        self.bounds = Bounds()
        self.new_mino()

    def render(self):
        """
        Render UI
        """
        # Render to board
        self.board.clear_tiles()
        self.board.draw_tiles(self.mino.tiles, self.mino.color)
        self.board.draw_tiles(self.mino.left_bound, '#aaa')
        self.board.draw_tiles(self.mino.right_bound, '#aaa')
        self.board.draw_tiles(self.mino.down_bound, '#aaa')

    def new_mino(self):
        """
        Initialize new mino
        """
        self.mino = Mino.random()
        self.render()

    def clock_tick_update(self):
        """
        Docstring for clock_tick_update
        """
        if self.bounds.down_bound.is_outside(self.mino.down_bound):
            self.new_mino()
        else:
            self.move_down()

    def rotate(self, event):
        """
        Rotate current mino
        """
        print('Rotate called')
        self.mino.orientation = (self.mino.orientation + 1) % 4
        self.render()

    def move_left(self, event=None):
        """
        Move current mino left
        """
        print('Move left called')
        if self.bounds.left_bound.is_within(self.mino.left_bound):
            self.mino.position += np.array([0, -1])
            self.render()

    def move_right(self, event=None):
        """
        Move current mino right
        """
        print('Move right called')
        if self.bounds.right_bound.is_within(self.mino.right_bound):
            self.mino.position += np.array([0, 1])
            self.render()

    def move_down(self, event=None):
        """
        Move current mino down
        """
        print('Move down called')
        if self.bounds.down_bound.is_within(self.mino.down_bound):
            self.mino.position += np.array([1, 0])
            self.render()
