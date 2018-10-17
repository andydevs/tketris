"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np

class RotateAction:
    """
    Docstring for RotateAction
    """
    def can_rotate(self):
        """
        Docstring for can_rotate
        """
        return self.game_continue

    def rotate(self, event):
        """
        Rotate current mino
        """
        if self.can_rotate():
            self.mino.orientation = (self.mino.orientation + 1) % 4
            self.render()

class MoveLeftAction:
    """
    Docstring for MoveLeftAction
    """
    def can_move_left(self):
        """
        True if the current mino can move left
        """
        return self.game_continue and not (
            self.bounds.left_bound.collision(self.mino.tiles) \
            or self.board_tileset.right_bound.collision(self.mino.tiles)
        )

    def move_left(self, event):
        """
        Move current mino left
        """
        if self.can_move_left():
            self.mino.position += np.array([0, -1])
            self.render()

class MoveRightAction:
    """
    Docstring for MoveRightAction
    """
    def can_move_right(self):
        """
        True if the current mino can move right
        """
        return self.game_continue and not (
            self.bounds.right_bound.collision(self.mino.tiles) \
            or self.board_tileset.left_bound.collision(self.mino.tiles)
        )

    def move_right(self, event):
        """
        Move current mino right
        """
        if self.can_move_right():
            self.mino.position += np.array([0, 1])
            self.render()

class MoveDownAction:
    """
    Docstring for MoveDownAction
    """
    def can_move_down(self):
        """
        True if the current mino can move down
        """
        return self.game_continue and not (
            self.bounds.down_bound.collision(self.mino.tiles) \
            or self.board_tileset.up_bound.collision(self.mino.tiles)
        )

    def move_down(self, event):
        """
        Move current mino down
        """
        if self.can_move_down():
            self.mino.position += np.array([1, 0])
            self.render()
