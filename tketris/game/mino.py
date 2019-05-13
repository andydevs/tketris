"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from random import choice as random_choice
from ..numpy_algorithms import transform_tileset

"""
The tetris mino classes. In tketris, Minos are represented as objects
containing the basic set of tiles comprising the mino shape, as well
as the current position and orientation of the Mino. Mino objects
have a method which automatically calculates the tiles to draw
when rendering.
"""

class Mino:
    """
    Mino abstraction. This class contains the class method 'new_mino' which
    generates a new subclass for a particular mino type given the type's
    information, used below. This method also appends the new mino type to
    the minos array, which is used in the 'random' method.

    The 'random' method returns a random mino at the given position and
    orientation (default at the top middle at orientation 0).
    """
    DEBUG = False

    # The minos array. 'random' picks a mino type from this array
    minos = []

    @classmethod
    def new_type(cls, name, color, shape):
        """
        Creates a new mino type and saves it to the minos array.

        :param name: the name of the new mino type
        :param color: the tile color of the mino type
        :param shape: the shape tileset of the mino type (centered at 0,0)
        """
        mtype = type(name, (Mino,), {
            'color':color,
            'shape':np.array(shape, dtype=int)
        })
        cls.minos.append(mtype)
        return mtype

    @classmethod
    def random(cls, position=(0, 4), orientation=0, debug=False):
        """
        Returns a random new mino at the given position and orientation

        :param position: initial position of new mino (default to top center)
        :param orientation: orientation of new mino (default to top center)

        :return: random new mino at position and orientation
        """
        return random_choice(cls.minos)(position, orientation, debug)

    def __init__(self, position=(0, 4), orientation=0, debug=False):
        """
        Initializes new Mino at given position and orientation

        :param position: initial position of new mino (default to top center)
        :param orientation: orientation of new mino (default to top center)
        """
        self.position = np.array(position)
        self.orientation = orientation
        self.DEBUG = debug

    @property
    def tiles(self):
        """
        The absolute tile positions of the mino
        """
        # Transform tileset
        return transform_tileset(
            self.position,
            self.orientation,
            self.shape,
            debug=self.DEBUG)

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
