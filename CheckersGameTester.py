# Author: Jonathan Hirsch
# GitHub username: Jon-H03
# Date: 3/19/2023
# Description: CheckersGameTester.py is a file that contains 5 separate unit test that ensure correct function of specific
# parts of the CheckersGame.py file.

from CheckersGame import *
import unittest


class UnitTest(unittest.TestCase):
    def test_piece_movement(self):
        """Tests if piece movement works and is accurate."""
        checkers = Checkers()
        player1 = checkers.create_player("Jon", "Black")
        player2 = checkers.create_player("Kathleen", "White")

        checkers.play_game("Jon", (5, 0), (4, 1))
        self.assertEqual(checkers.get_checker_details((4, 1)), "Black")

    def test_piece_capture(self):
        """Tests if a piece is hopped over, it is captured."""
        checkers = Checkers()
        player1 = checkers.create_player("Jon", "Black")
        player2 = checkers.create_player("Kathleen", "White")

        checkers.play_game("Jon", (5, 0), (4, 1))
        checkers.play_game("Kathleen", (2, 1), (3, 2))
        checkers.play_game("Jon", (5, 6), (4, 7))
        checkers.play_game("Kathleen", (3, 2), (5, 0))

        self.assertNotEqual(checkers.get_checker_details((4, 1)), "Black")

    def test_piece_to_king(self):
        """Tests if a piece makes it to the other side, it becomes a king."""
        checkers = Checkers()
        player1 = checkers.create_player("Jon", "Black")
        player2 = checkers.create_player("Kathleen", "White")

        checkers.play_game("Jon", (5, 0), (4, 1))
        checkers.play_game("Kathleen", (2, 1), (3, 2))
        checkers.play_game("Jon", (5, 6), (4, 7))
        checkers.play_game("Kathleen", (3, 2), (5, 0))
        checkers.play_game("Jon", (5, 2), (4, 1))
        checkers.play_game("Kathleen", (2, 3), (3, 4))
        checkers.play_game("Jon", (6, 1), (5, 2))
        checkers.play_game("Kathleen", (3, 4), (2, 3))
        checkers.play_game("Jon", (5, 2), (4, 3))
        checkers.play_game("Kathleen", (2, 5), (3, 6))
        checkers.play_game("Jon", (6, 3), (5, 2))
        checkers.play_game("Kathleen", (1, 0), (2, 1))
        checkers.play_game("Jon", (7, 2), (6, 3))
        checkers.play_game("Kathleen", (5, 0), (6, 1))
        checkers.play_game("Jon", (4, 3), (2, 5))
        checkers.play_game("Kathleen", (6, 1), (7, 2))

        self.assertEqual(checkers.get_checker_details((7, 2)), "White_king")

    def test_king_to_triple_king(self):
        """Tests if a king makes it back to its own side, it becomes a Triple King."""
        checkers = Checkers()
        player1 = checkers.create_player("Jon", "Black")
        player2 = checkers.create_player("Kathleen", "White")

        checkers._board.update_board((7, 0), None)
        checkers._board.update_board((6, 1), "Black_king")

        checkers.play_game("Jon", (6, 1), (7, 0))

        self.assertEqual(checkers.get_checker_details((7, 0)), "Black_Triple_King")

    def test_winner(self):
        """Tests if game_winner() method functions as intended."""
        checkers = Checkers()
        player1 = checkers.create_player("Jon", "Black")
        player2 = checkers.create_player("Kathleen", "White")

        for i in range(12):
            player1.add_captured_piece()

        self.assertNotEqual(checkers.game_winner(), "Kathleen")