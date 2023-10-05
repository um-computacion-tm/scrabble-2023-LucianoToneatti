import unittest
from game.scrabble import Scrabble
from game.models import Tile

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
        game = Scrabble(2)    
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[1])   
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
    def test_validate_word(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        self.assertEqual(game.scrabble_validate_word(word,location,orientation), True)

    def test_scrabble_validate_word(self):
        game = Scrabble(2)
        result = game.scrabble_validate_word("PYTHON", (0, 0), "H")
        self.assertEqual(result, True)  

    def test_scrabble_string_to_tiles(self):
        expected_tiles_data = [
            ('P', 2),
            ('Y', 4),
            ('T', 1),
            ('H', 4),
            ('O', 1),
            ('N', 1)
        ]
        expected_tiles = [Tile(letter=letter, value=value) for letter, value in expected_tiles_data]
        game = Scrabble(2)  
        result = game.scrabble_string_to_tiles("PYTHON")
        self.assertEqual([tile.letter for tile in result], [tile.letter for tile in expected_tiles])
        self.assertEqual([tile.value for tile in result], [tile.value for tile in expected_tiles])

if __name__ == '__main__':
    unittest.main()