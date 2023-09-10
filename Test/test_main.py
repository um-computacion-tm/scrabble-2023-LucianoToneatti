import unittest
from unittest.mock import patch
from io import StringIO
from main import ScrabbleGame
class TestScrabbleGame(unittest.TestCase):    
    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_scrabble_game_with_valid_input(self, mock_stdout, mock_input):
        game = ScrabbleGame()
        game.run()
        expected_output = 'Bienvenido\nLa cantidad de jugadores es: 3\nTurno del jugador 1\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)
if __name__ == '__main__':
    unittest.main()