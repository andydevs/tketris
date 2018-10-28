"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from functools import reduce
import numpy as np

def tile_in_set(tiles_a, tiles_b):
    """
    Returns an array of booleans which are true if the tile in that row matches
    any of the tiles in the other tileset

    :param tiles_a: the first tileset being checked
    :param tiles_b: the second tileset being checked

    :return: an array of booleans which are true if the tile in that row matches
             any of the tiles in the other tileset
    """
    # Return false if any of the arguments have no dimension
    if tiles_a.shape[0] == 0 or tiles_b.shape[0] == 0:
        return False
    else:
        # Expand arrays into third dimension
        expanded_a = np.expand_dims(tiles_a, axis=1)
        expanded_b = np.expand_dims(tiles_b, axis=0)

        # Check equality of point pairs
        point_pair_equal = np.all(np.equal(expanded_a, expanded_b), axis=2)

        # Return flattened array of checks for each point pair
        return np.any(point_pair_equal, axis=1).flatten()


def tileset_intersection(tiles_a, tiles_b):
    """
    Checks for an intersection in the given tiles, i.e. if any tile in the
    first tileset matches a tile in the second tileset

    :param tiles_a: the first tileset being checked
    :param tiles_b: the second tileset being checked

    :return: true if there is an intersection
    """
    # Check for tiles in set
    tiles_in_set = tile_in_set(tiles_a, tiles_b)

    # Check if any point pairs are equal
    return np.any(tiles_in_set)


def transform_tileset(pos, rot, tiles):
    """
    Returns the transformed tileset, at the correct position and rotation

    :param pos: the position offset of the tiles
    :param rot: the rotation integer of the tiles
    :param tiles: the tiles to transform

    :return: transformed tiles
    """
    # Transform matrix
    transform_matrix = np.matrix([
        [ np.cos(rot*np.pi/2), np.sin(rot*np.pi/2), 0],
        [-np.sin(rot*np.pi/2), np.cos(rot*np.pi/2), 0],
        [ pos[0],              pos[1],              1]
    ])

    # Homogenous tiles array
    one_column = np.ones((tiles.shape[0], 1))
    homogenous_tiles = np.concatenate((tiles, one_column), axis=1)

    # Multiply homogenous vector array by transform matrix
    transformed_homogenous_tiles = np.matmul(homogenous_tiles, transform_matrix)

    # Return tiles extracted from transformed homogenous tiles
    return transformed_homogenous_tiles[:,0:2].astype(int)
