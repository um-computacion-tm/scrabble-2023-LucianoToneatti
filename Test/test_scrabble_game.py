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

if __name__ == '__main__':
    unittest.main()