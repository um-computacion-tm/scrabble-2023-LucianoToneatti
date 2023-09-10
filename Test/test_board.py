import unittest
from game.board import Board
from game.models import Tile
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,5)

    def _test_with_multiplier(self, multiplier_type, expected_value):
        board = Board()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type=multiplier_type),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, expected_value)    
    def test_with_letter_multiplayer(self):
        self._test_with_multiplier('letter', 7)    
    def test_with_word_multiplayer(self):
        self._test_with_multiplier('word', 10)

    def test_with_word_and_letter_multiplayer(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,14)
    def test_with_word_and_letter_multiplayer_no_active(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,5)

if __name__ == '__main__':
    unittest.main()