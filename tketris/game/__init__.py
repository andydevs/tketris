"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import BoardBounds, TileSetBound
from .tileset import BoardTileSet
from .actions import RotateAction, MoveLeftAction, MoveRightAction, MoveDownAction
from .mino import Mino

class GameLogic(RotateAction, MoveLeftAction, MoveRightAction, MoveDownAction):
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

    def clear_tiles(self):
        """
        Docstring for clear_tiles
        """
        self.board_tileset.clear_tiles()

    def new_mino(self):
        """
        Initialize new mino
        """
        self.mino = Mino.random()
        self.render()

    def new_round(self):
        """
        Docstring for new_round
        """
        self.board_tileset.add_tiles(self.mino.tiles, self.mino.color)
        self.board_tileset.clear_rows()
        self.new_mino()
        if not self.can_move_down():
            self.game_continue = False
            self.game_over()

    def clock_tick_update(self):
        """
        Docstring for clock_tick_update
        """
        if not self.can_move_down():
            self.new_round()
        else:
            self.move_down(None)

    def game_over(self):
        """
        Docstring for game_over
        """
        pass
