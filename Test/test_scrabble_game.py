import unittest
from game.scrabble import Scrabble
from game.player import Player
from game.board import Board

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = Scrabble(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
        self.assertEqual(scrabble_1.turn, 1)
    def test_unique_id(self):
        game_1 = Scrabble(1)
        game_2 = Scrabble(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)
    def test_next_turn_when_game_is_starling(self):
        game = Scrabble(2)
        game.next_turn()
        self.assertEqual(game.current_player,game.players[0])
    def test_next_turn_when_game_is_not_the_first_and_is_last(self):
        game = Scrabble(2)    # Test when game is not the first
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[1])    # Test when game is last
        game.current_player = game.players[1]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])
    def test_next_turn(self):
        game = Scrabble(2)
        self.assertEqual(game.turn, 1)
        game.next_turn()
        self.assertEqual(game.turn, 2)
    def test_playing(self):
        game = Scrabble(1)
        self.assertEqual(game.playing(), True)

if __name__ == '__main__':
    unittest.main()