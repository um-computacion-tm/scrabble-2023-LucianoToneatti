import unittest
from game.board import Board
from game.models import Tile
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

    def test_word_inside_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)

    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertEqual(word_is_valid, True)

    def test_word_out_of_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_word_out_of_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 14)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty(), True)

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7] = Tile('C', 1)
        self.assertEqual(board.is_empty(), False)

    def test_is_active_and_letter_multiplier(self):
        board = Board()
        cell1 = Cell(status='active', multiplier_type='letter')
        cell2 = Cell(status='active', multiplier_type='word')
        cell3 = Cell(status='desactive', multiplier_type='letter')
        cell4 = Cell(status='desactive', multiplier_type='word')

        self.assertTrue(board.is_active_and_letter_multiplier(cell1))
        self.assertFalse(board.is_active_and_letter_multiplier(cell2))
        self.assertFalse(board.is_active_and_letter_multiplier(cell3))
        self.assertFalse(board.is_active_and_letter_multiplier(cell4))

    def test_is_active_and_word_multiplier(self):
        board = Board()
        cell1 = Cell(status='active', multiplier_type='word')
        cell2 = Cell(status='active', multiplier_type='letter')
        cell3 = Cell(status='desactive', multiplier_type='word')
        cell4 = Cell(status='desactive', multiplier_type='letter')

        self.assertTrue(board.is_active_and_word_multiplier(cell1))
        self.assertFalse(board.is_active_and_word_multiplier(cell2))
        self.assertFalse(board.is_active_and_word_multiplier(cell3))
        self.assertFalse(board.is_active_and_word_multiplier(cell4))

    def test_is_desactive_or_none_multiplier(self):
        board = Board()
        cell1 = Cell(status='desactive', multiplier_type='')
        cell2 = Cell(status='active', multiplier_type='')
        cell3 = Cell(status='desactive', multiplier_type='letter')
        cell4 = Cell(status='desactive', multiplier_type='word')

        self.assertTrue(board.is_desactive_or_none_multiplier(cell1))
        self.assertTrue(board.is_desactive_or_none_multiplier(cell2))
        self.assertTrue(board.is_desactive_or_none_multiplier(cell3))
        self.assertTrue(board.is_desactive_or_none_multiplier(cell4))

    def test_calculate_word_value(self):
        board = Board()
        cell1 = Cell(letter=Tile('C', 1))
        cell2 = Cell(letter=Tile('A', 1))
        cell3 = Cell(letter=Tile('S', 2), multiplier=2, multiplier_type='letter')
        cell4 = Cell(letter=Tile('A', 1))
        cell5 = Cell(letter=Tile('W', 3), multiplier=3, multiplier_type='word')

        word1 = [cell1, cell2, cell3, cell4]
        word2 = [cell1, cell2, cell3, cell4, cell5]

        self.assertEqual(board.calculate_word_value(word1), 7)
        self.assertEqual(board.calculate_word_value(word2), 30)

    def test_validate_word_place_board(self):
        pass

if __name__ == '__main__':
    unittest.main()