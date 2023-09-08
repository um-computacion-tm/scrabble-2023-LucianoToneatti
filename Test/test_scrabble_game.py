import unittest
from game.scrabble import Scrabble
from game.player import Player

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = Scrabble(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
        self.assertEqual(scrabble_1.turn, 0)
    def test_unique_id(self):
        game_1 = Scrabble(1)
        game_2 = Scrabble(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)

    def test_next_turn(self):
        game = Scrabble(2)
        self.assertEqual(game.turn, 0)
        game.next_turn()
        self.assertEqual(game.turn, 1)
    def test_playing(self):
        game = Scrabble(1)
        self.assertEqual(game.playing(), True)

if __name__ == '__main__':
    unittest.main()