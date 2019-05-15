"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
import numpy as np
from .bounds import BoardBounds, BoardRotateBounds, TileSetBound
from .tileset import BoardTileSet
from .controller import Controller
from .mino import Mino

class GameLogic(Controller):
    """
    MIXIN

    Main Tketris Game Logic. All of the magic happens here!
    Well... most of the magic... just the game logic, as the name suggests...
    """
    def init_game(self):
        """
        Initialize game logic
        """
        self.bounds = BoardBounds()
        self.rotate_bounds = BoardRotateBounds()
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
            self.board.draw_tiles(self.bounds.left_bound.tiles, '#ccc')
            self.board.draw_tiles(self.bounds.right_bound.tiles, '#ccc')
            self.board.draw_tiles(self.bounds.down_bound.tiles, '#ccc')

            # Draw boundaries of board tiles
            self.board.draw_tiles(self.board_tileset.left_bound.tiles, '#ccc')
            self.board.draw_tiles(self.board_tileset.right_bound.tiles, '#ccc')
            self.board.draw_tiles(self.board_tileset.up_bound.tiles, '#ccc')

        # Render tiles on ground
        for i, j, color in self.board_tileset.tile_colors:
            self.board.draw_tile((i, j), color)

        # Render current mino
        self.board.draw_tiles(self.mino.tiles, self.mino.color)

    def clear_tiles(self):
        """
        Clear tiles on the board
        """
        self.board_tileset.clear_tiles()

    def add_mino_to_board(self):
        """
        Adds mino to board tileset, clears required rows,
        and adds row score to the total score
        """
        self.board_tileset.add_tiles(self.mino.tiles, self.mino.color)
        rows = self.board_tileset.clear_rows()
        self.row_score(rows)

    def new_round(self):
        """
        Creates a new mino, starting a new round
        (trigger game over if new mino can't move down)
        """
        self.mino = Mino.random(debug=self.DEBUG)
        self.render()
        if not self.can_move_down():
            self.game_continue = False
            self.on_game_over()

    def soft_drop(self):
        """
        Add soft drop score
        """
        self.score += 4
        self.on_update_score()

    def row_score(self, rows):
        """
        Compute row score given number of cleared rows

        :param rows: number of cleared rows
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
        Update every clock tick. If mino can't move down, add soft drop score,
        add mino to board, and start new round. Else just move the mino down.
        """
        if not self.can_move_down():
            self.soft_drop()
            self.add_mino_to_board()
            self.new_round()
        else:
            self.move_down(None)

    def start_game(self):
        """
        Start new game. Reset board and score. Set flags. Start new round.
        """
        self.score = 0
        self.board_tileset.clear_tiles()
        self.game_continue = True
        self.game_resume = True
        self.new_round()
        self.on_start_game()

    def on_start_game(self):
        """
        HOOK

        Called after game starts
        """
        pass

    def on_game_over(self):
        """
        HOOK

        Called after game over
        """
        pass

    def on_update_score(self, score):
        """
        HOOK

        Called after score updates
        """
        pass
