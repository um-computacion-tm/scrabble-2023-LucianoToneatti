import unittest
from game.several import Several
from game.cell import Cell
from game.models import Tile

class TestSeveral(unittest.TestCase):
    
    def test_converter_word_special_CHOCOLATE(self):
        sev = Several()
        list_tiles = sev.board_string_to_tiles("CHOCOLATE")
        self.assertEqual(list_tiles[0].letter, "CH")
        self.assertEqual(list_tiles[0].value, 5)  
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "C")
        self.assertEqual(list_tiles[2].value, 2)  
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "L")
        self.assertEqual(list_tiles[4].value, 1)
        self.assertEqual(list_tiles[5].letter, "A")
        self.assertEqual(list_tiles[5].value, 1)
        self.assertEqual(list_tiles[6].letter, "T")
        self.assertEqual(list_tiles[6].value, 1)
        self.assertEqual(list_tiles[7].letter, "E")
        self.assertEqual(list_tiles[7].value, 1)

    def test_converter_word_special_LLANTO(self):
        sev = Several()
        list_tiles = sev.board_string_to_tiles("LLANTO")
        self.assertEqual(list_tiles[0].letter, "LL")
        self.assertEqual(list_tiles[0].value, 8)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "N")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "T")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "O")
        self.assertEqual(list_tiles[4].value, 1)
        
    def test_converter_word_special_TARRO(self):
        sev = Several()
        list_tiles = sev.board_string_to_tiles("TARRO")
        self.assertEqual(list_tiles[0].letter, "T")
        self.assertEqual(list_tiles[0].value, 1)  
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "RR")
        self.assertEqual(list_tiles[2].value, 8)
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)  

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
        sev = Several()  
        result = sev.board_string_to_tiles("PYTHON")
        self.assertEqual([tile.letter for tile in result], [tile.letter for tile in expected_tiles])
        self.assertEqual([tile.value for tile in result], [tile.value for tile in expected_tiles])

 
    def test_simple(self):
        sev = Several()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = sev.calculate_word_value(word)
        self.assertEqual(value,5)
    def test_with_letter_multiplayer(self):
        sev = Several()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A',1))
        ]
        value = sev.calculate_word_value(word)
        self.assertEqual(value,7)

    def test_with_word_multiplayer(self):
        sev = Several()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = sev.calculate_word_value(word)
        self.assertEqual(value,10)
    def test_with_word_and_letter_multiplayer(self):
        sev = Several()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = sev.calculate_word_value(word)
        self.assertEqual(value,14)
    def test_with_word_and_letter_multiplayer_no_active(self):
        sev = Several()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = sev.calculate_word_value(word)
        self.assertEqual(value,5)

    def test_string_to_tiles(self):
        several = Several()
        result_list = []
        input_string = "HELLO"
        several.string_to_tiles(input_string, result_list)
        expected_letters = set("HELLO")
        for tile in result_list:
            self.assertTrue(tile.letter in expected_letters)
