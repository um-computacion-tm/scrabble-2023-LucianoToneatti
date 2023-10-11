import unittest
from game.scrabble import Scrabble
from game.cell import Cell
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

    def test_calculate_score_word_with_single_letter(self):
        game = Scrabble(2)
        # Define una palabra que contiene una única letra 'A' en una casilla con multiplicador de palabra 1 y valor de letra 1.
        word = [Cell(multiplier=1, letter=Tile("A", 1))]
        game.next_turn()
        # Verifica que la puntuación del jugador actual sea 0 al inicio.
        self.assertEqual(game.current_player.score, 0)
        game.scrabble_word_calculate_score(word)
        self.assertEqual(game.current_player.score, 1)

    def test_calculate_score_word_with_existing_score(self):
        game = Scrabble(2)
        # Define una palabra que contiene una única letra 'Z' en una casilla con multiplicador de palabra 2 y valor de letra 10.
        word = [Cell(multiplier=2, letter=Tile("Z", 10))]
        game.next_turn()
        # Establece manualmente la puntuación del jugador actual en 5.
        game.current_player.score = 5
        game.scrabble_word_calculate_score(word)
        self.assertEqual(game.current_player.score, 25)

    #ESTOS TEST SON PARA CUBRIR AL def scrabble_string_to_tiles pero todavia no logro que lo cubran correctamente

    """def test_single_letter_conversion_agua(self):
        game = Scrabble(2)
        input_string = "agua"
        expected_tiles = [
            Tile('A', 1),
            Tile('G', 2),
            Tile('U', 1),
            Tile('A', 1)
        ]
        tiles = game.scrabble_string_to_tiles(input_string)
        self.assertEqual([tile.letter for tile in tiles], [tile.letter for tile in expected_tiles])

    def test_single_letter_conversion_moco(self):
        game = Scrabble(2)
        input_string = "moco"
        expected_tiles = [
            Tile('M', 3),
            Tile('O', 1),
            Tile('C', 2),
            Tile('O', 1)
        ]
        tiles = game.scrabble_string_to_tiles(input_string)
        self.assertEqual([tile.letter for tile in tiles], [tile.letter for tile in expected_tiles])
    """

    


if __name__ == '__main__':
    unittest.main()