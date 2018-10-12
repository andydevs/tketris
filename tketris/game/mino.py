"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from random import choice as random_choice

class Mino:
    """
    Mino abstraction
    """
    minos = []

    @classmethod
    def new_type(cls, name, color, shape):
        """
        Creates a new mino type with the given name color shape
        """
        mtype = type(name, (Mino,), {
            'color':color,
            'shape':np.array(shape)
        })
        cls.minos.append(mtype)
        return mtype

    @classmethod
    def random(cls, position=(0, 4), orientation=0):
        """
        Returns a random new mino
        """
        return random_choice(cls.minos)(position, orientation)

    def __init__(self, position=(0, 4), orientation=0):
        """
        Initializes instance
        """
        self.position = np.array(position)
        self.orientation = orientation

    @property
    def orientrix(self):
        """
        Orientation matrix
        """
        return np.linalg.matrix_power(
            np.array([[0, 1], [-1, 0]]),
            self.orientation)

    @property
    def tiles(self):
        """
        The absolute tile positions of the mino
        """
        return np.add(np.dot(self.shape, self.orientrix), self.position)

    @property
    def left_bound(self):
        """
        Left boundary of mino
        """
        # Get all unique rows in mino
        rows = {tile[0] for tile in self.tiles}

        # Find leftmost tile for each row
        boundary_tiles = [
            (row, min(tile[1] for tile in self.tiles if tile[0] == row) )
            for row in rows
        ]

        # Return one left of leftmost tiles
        return np.array([ (row, column - 1) for row, column in boundary_tiles ])

    @property
    def right_bound(self):
        """
        Right boundary of mino
        """
        # Get all unique rows in mino
        rows = {tile[0] for tile in self.tiles}

        # Find rightmost tile for each row
        boundary_tiles = [
            (row, max(tile[1] for tile in self.tiles if tile[0] == row))
            for row in rows
        ]

        # Return one right of rightmost tile
        return np.array([ (row, column + 1) for row, column in boundary_tiles ])

    @property
    def down_bound(self):
        """
        Down boundary of mino
        """
        # Get all unique columns in mino
        columns = {tile[1] for tile in self.tiles}

        # Find lowest tile for each column
        boundary_tiles = [
            (max(tile[0] for tile in self.tiles if tile[1] == column), column)
            for column in columns
        ]

        # Return one below lowest tile
        return np.array([ (row + 1, column) for row, column in boundary_tiles ])

# Mino types
IMino = Mino.new_type('IMino', '#00bbff', [
    [-1, 0],
    [ 0, 0],
    [ 1, 0],
    [ 2, 0]
])
JMino = Mino.new_type('JMino', '#3300ff', [
    [-1,  0],
    [ 0,  0],
    [ 1,  0],
    [ 1, -1]
])
LMino = Mino.new_type('LMino', '#ff6600', [
    [-1,  0],
    [ 0,  0],
    [ 1,  0],
    [ 1,  1]
])
TMino = Mino.new_type('TMino', '#ff00ff', [
    [0, -1],
    [0,  0],
    [0,  1],
    [1,  0]
])
SMino = Mino.new_type('SMino', '#ff0000', [
    [1, -1],
    [1,  0],
    [0,  0],
    [0,  1]
])
ZMino = Mino.new_type('ZMino', '#00aa00', [
    [0, -1],
    [0,  0],
    [1,  0],
    [1,  1]
])
OMino = Mino.new_type('OMino', '#999900', [
    [0, -1],
    [0,  0],
    [1, -1],
    [1,  0]
])
