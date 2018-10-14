"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import BoardBounds, TileSetBound
from .tileset import BoardTileSet
from .mino import Mino, IMino, JMino, SMino

class GameLogic:
    """
    Tketris Game Logic mixin
    """
    def init_game(self):
        """
        Initialize game
        """
        self.bounds = BoardBounds()
        self.board_tileset = BoardTileSet([
            (19, 1, SMino.color),
            (18, 1, JMino.color),
            (17, 1, JMino.color),
            (17, 2, JMino.color),
            (19, 4, IMino.color),
            (19, 5, SMino.color)
        ])
        self.new_mino()

    def render(self):
        """
        Render UI
        """
        # Clear all tiles in board
        self.board.clear_tiles()

        # Draw boundaries of tiles
        self.board.draw_tiles(self.board_tileset.left_bound.tiles, '#faa')
        self.board.draw_tiles(self.board_tileset.right_bound.tiles, '#afa')
        self.board.draw_tiles(self.board_tileset.up_bound.tiles, '#aaf')

        # Draw boundaries of mino
        self.board.draw_tiles(self.mino.left_bound, '#faa')
        self.board.draw_tiles(self.mino.right_bound, '#afa')
        self.board.draw_tiles(self.mino.down_bound, '#aaf')

        # Render tiles on ground
        for i, j, color in self.board_tileset.tile_colors:
            self.board.draw_tile((i, j), color)

        # Render current mino
        self.board.draw_tiles(self.mino.tiles, self.mino.color)

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
        self.move_down()

    def rotate(self, event):
        """
        Rotate current mino
        """
        self.mino.orientation = (self.mino.orientation + 1) % 4
        self.render()

    def can_move_left(self):
        """
        True if the current mino can move left
        """
        return self.bounds.left_bound.is_within(self.mino.left_bound) \
            and not self.board_tileset.right_bound.collision(self.mino.tiles)

    def move_left(self, event=None):
        """
        Move current mino left
        """
        if self.can_move_left():
            self.mino.position += np.array([0, -1])
            self.render()

    def can_move_right(self):
        """
        True if the current mino can move right
        """
        return self.bounds.right_bound.is_within(self.mino.right_bound) \
            and not self.board_tileset.left_bound.collision(self.mino.tiles)

    def move_right(self, event=None):
        """
        Move current mino right
        """
        if self.can_move_right():
            self.mino.position += np.array([0, 1])
            self.render()

    def can_move_down(self):
        """
        True if the current mino can move down
        """
        return self.bounds.down_bound.is_within(self.mino.down_bound) \
            and not self.board_tileset.up_bound.collision(self.mino.tiles)

    def move_down(self, event=None):
        """
        Move current mino down
        """
        if self.can_move_down():
            self.mino.position += np.array([1, 0])
            self.render()
