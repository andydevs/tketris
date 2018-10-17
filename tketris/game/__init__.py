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
        self.board_tileset = BoardTileSet([])
        self.new_mino()

    def render(self):
        """
        Render UI
        """
        # Clear all tiles in board
        self.board.clear_tiles()

        # If debugging
        if self.DEBUG:
            # Draw boundaries of board
            self.board.draw_tiles(self.bounds.left_bound.tiles, '#faa')
            self.board.draw_tiles(self.bounds.right_bound.tiles, '#afa')
            self.board.draw_tiles(self.bounds.down_bound.tiles, '#aaf')

            # Draw boundaries of board tiles
            self.board.draw_tiles(self.board_tileset.left_bound.tiles, '#faa')
            self.board.draw_tiles(self.board_tileset.right_bound.tiles, '#afa')
            self.board.draw_tiles(self.board_tileset.up_bound.tiles, '#aaf')

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
        if not self.can_move_down():
            self.board_tileset.add_tiles(self.mino.tiles, self.mino.color)
            self.board_tileset.clear_rows()
            self.new_mino()
            if not self.can_move_down():
                self.game_continue = False
                self.game_over_event()
        else:
            self.move_down()

    def rotate(self):
        """
        Rotate current mino
        """
        self.mino.orientation = (self.mino.orientation + 1) % 4
        self.render()

    def can_move_left(self):
        """
        True if the current mino can move left
        """
        return not (
            self.bounds.left_bound.collision(self.mino.tiles) \
            or self.board_tileset.right_bound.collision(self.mino.tiles)
        )

    def move_left(self):
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
        return not (
            self.bounds.right_bound.collision(self.mino.tiles) \
            or self.board_tileset.left_bound.collision(self.mino.tiles)
        )

    def move_right(self):
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
        return not (
            self.bounds.down_bound.collision(self.mino.tiles) \
            or self.board_tileset.up_bound.collision(self.mino.tiles)
        )

    def move_down(self):
        """
        Move current mino down
        """
        if self.can_move_down():
            self.mino.position += np.array([1, 0])
            self.render()

    def game_over_event(self):
        """
        Docstring for game_over_event
        """
        pass
