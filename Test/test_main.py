import unittest
from game import main
from unittest.mock import patch


class TestMain(unittest.TestCase):
    pass
    '''@patch('builtins.input', side_effect=["2"])
    def test_player_count(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
        mock_print.assert_called_once_with('Scrabble iniciad con 2 jugadores')'''
if __name__ == '__main__':
    unittest.main()