import unittest
import sys
from main import Main
from unittest.mock import patch
from io import StringIO


class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout
    @patch('builtins.input', side_effect=['3']) 

    def test_vaild_player_count_input(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)
    @patch('builtins.input', side_effect=['3']) 
    
    def test_player_count_input_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Saludos y bienvenidos', main_output_value)
        self.assertIn('Número de participantes es: 3', main_output_value)
        self.assertIn('Turno del participante 1', main_output_value)
    @patch('builtins.input', side_effect=['5','3'])

    def test_player_count_input_invalid_then_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Saludos y bienvenidos', main_output_value)
        self.assertIn('Valor ingresado no valido', main_output_value)
        self.assertIn('Número de participantes es: 3', main_output_value)
        self.assertIn('Turno del participante 1', main_output_value)

if __name__ == '__main__':
    unittest.main()