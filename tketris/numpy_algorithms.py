"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np

"""
Helper methods for tketris systems that use numpy (pretty much the tilesets).
"""

def tile_in_set(tiles_a, tiles_b):
    """
    Returns an array of booleans which indicate if the corresponding tile
    in the first tileset is found in the second tileset

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


def transform_tileset(pos, rot, tiles, debug=False):
    """
    Returns the transformed tileset, at the correct position and rotation

    :param pos: the position offset of the tiles
    :param rot: the rotation integer of the tiles
    :param tiles: the tiles to transform

    :return: transformed tiles
    """
    # Debug initial
    if debug:
        print('-----------------------TRANSFORM TILESET-----------------------')
        print('Position:', pos)
        print('Rotation:', rot)
        print('Tiles:')
        print(tiles)

    # Transform matrix
    isin = [0,  1,  0, -1]
    icos = [1,  0, -1,  0]
    transform_matrix = np.matrix([
        [  icos[rot],   isin[rot], 0 ],
        [ -isin[rot],   icos[rot], 0 ],
        [  pos[0],      pos[1],    1 ]
    ])

    # Homogenous tiles array
    one_column = np.ones((tiles.shape[0], 1))
    homogenous_tiles = np.concatenate((tiles, one_column), axis=1)

    # Get transformed tiles
    transformed_tiles = np.matmul(homogenous_tiles, transform_matrix)
    transformed_tiles = transformed_tiles.astype(int)[:,0:2]

    # Transformed tiles debug
    if debug:
        print('Transformed Tileset:')
        print(transformed_tiles)

    # Return tiles extracted from transformed homogenous tiles
    return transformed_tiles
