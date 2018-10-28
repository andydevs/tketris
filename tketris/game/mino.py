"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from random import choice as random_choice
from ..numpy_algorithms import transform_tileset

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
            'shape':np.array(shape, dtype=int)
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
    def tiles(self):
        """
        The absolute tile positions of the mino
        """
        return transform_tileset(self.position, self.orientation, self.shape)

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
