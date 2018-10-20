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
        self.score = 0

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

    def add_mino_to_board(self):
        """
        Docstring for add_mino_to_board
        """
        self.board_tileset.add_tiles(self.mino.tiles, self.mino.color)
        rows = self.board_tileset.clear_rows()
        self.row_score(rows)

    def new_round(self):
        """
        Docstring for new_round
        """
        self.mino = Mino.random()
        self.render()
        if not self.can_move_down():
            self.game_continue = False
            self.on_game_over()

    def soft_drop(self):
        """
        Docstring for soft_drop
        """
        self.score += 4
        self.on_update_score()

    def row_score(self, rows):
        """
        Docstring for row_score
        """
        if rows == 1:
            self.score += 40
        elif rows == 2:
            self.score += 100
        elif rows == 3:
            self.score += 300
        elif rows == 4:
            self.score += 1200

        # Only call update score if score was actually updated
        if rows > 0:
            self.on_update_score()

    def clock_tick_update(self):
        """
        Docstring for clock_tick_update
        """
        if not self.can_move_down():
            self.soft_drop()
            self.add_mino_to_board()
            self.new_round()
        else:
            self.move_down(None)

    def start_game(self):
        """
        Docstring for start_game
        """
        self.score = 0
        self.board_tileset.clear_tiles()
        self.game_continue = True
        self.new_round()
        self.on_start_game()

    def on_start_game(self):
        """
        Docstring for on_start_game
        """
        pass

    def on_game_over(self):
        """
        Docstring for game_over
        """
        pass

    def on_update_score(self, score):
        """
        Docstring for update_score
        """
        pass
