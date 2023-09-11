from main import main
import unittest
from unittest.mock import patch
from io import StringIO


class TestScrabbleGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['3']) 
    def test_player_count_input_valid(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), 'Bienvenido\nLa cantidad de jugadores es: 3\nTurno del jugador 1\n')

    @patch('builtins.input', side_effect=['5', '3'])
    def test_player_count_input_invalid_then_valid(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            expected_output = 'Bienvenido\nValor invalido\nLa cantidad de jugadores es: 3\nTurno del jugador 1\n'
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()