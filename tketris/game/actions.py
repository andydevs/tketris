"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np

class Action:
    """
    Docstring for Action
    """
    def can_do_action(self):
        """
        Docstring for can_do_action
        """
        return self.game_continue and self.game_resume

class RotateAction(Action):
    """
    Docstring for RotateAction
    """
    def can_rotate(self):
        """
        Docstring for can_rotate
        """
        return self.can_do_action()

    def rotate(self, event):
        """
        Rotate current mino
        """
        if self.can_rotate():
            self.mino.orientation = (self.mino.orientation + 1) % 4
            self.render()

class MoveLeftAction(Action):
    """
    Docstring for MoveLeftAction
    """
    def can_move_left(self):
        """
        True if the current mino can move left
        """
        return self.can_do_action() and not (
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

class MoveRightAction(Action):
    """
    Docstring for MoveRightAction
    """
    def can_move_right(self):
        """
        True if the current mino can move right
        """
        return self.can_do_action() and not (
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

class MoveDownAction(Action):
    """
    Docstring for MoveDownAction
    """
    def can_move_down(self):
        """
        True if the current mino can move down
        """
        return self.can_do_action() and not (
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
