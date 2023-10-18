import unittest
from game.board import Board
from game.models import Tile
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid),15)
        self.assertEqual(len(board.grid[0]),15)

    def test_board_multiplier_word_in_board(self):
        board = Board()
        self.assertEqual(board.grid[0][0].multiplier, 3)
        self.assertEqual(board.grid[7][0].multiplier, 3)
        self.assertEqual(board.grid[14][0].multiplier, 3)
        self.assertEqual(board.grid[0][7].multiplier, 3)
        self.assertEqual(board.grid[0][14].multiplier, 3)
        self.assertEqual(board.grid[14][0].multiplier, 3)
        self.assertEqual(board.grid[14][7].multiplier, 3)
        self.assertEqual(board.grid[14][14].multiplier, 3)
        self.assertEqual(board.grid[1][1].multiplier, 2)
        self.assertEqual(board.grid[2][2].multiplier, 2)
        self.assertEqual(board.grid[3][3].multiplier, 2)
        self.assertEqual(board.grid[4][4].multiplier, 2)
        self.assertEqual(board.grid[13][1].multiplier, 2)
        self.assertEqual(board.grid[12][2].multiplier, 2)
        self.assertEqual(board.grid[11][3].multiplier, 2)
        self.assertEqual(board.grid[10][4].multiplier, 2)
        self.assertEqual(board.grid[1][13].multiplier, 2)
        self.assertEqual(board.grid[2][12].multiplier, 2)
        self.assertEqual(board.grid[3][11].multiplier, 2)
        self.assertEqual(board.grid[4][10].multiplier, 2)
        self.assertEqual(board.grid[13][13].multiplier, 2)
        self.assertEqual(board.grid[12][12].multiplier, 2)
        self.assertEqual(board.grid[11][11].multiplier, 2)
        self.assertEqual(board.grid[10][10].multiplier, 2)
        self.assertEqual(board.grid[7][7].multiplier, 2)

    def test_board_multiplier_letter_in_board(self):
        board = Board()
        self.assertEqual(board.grid[1][5].multiplier, 3)
        self.assertEqual(board.grid[1][9].multiplier, 3)
        self.assertEqual(board.grid[5][1].multiplier, 3)
        self.assertEqual(board.grid[5][5].multiplier, 3)
        self.assertEqual(board.grid[5][13].multiplier, 3)
        self.assertEqual(board.grid[9][1].multiplier, 3)
        self.assertEqual(board.grid[9][5].multiplier, 3)
        self.assertEqual(board.grid[9][9].multiplier, 3)
        self.assertEqual(board.grid[9][13].multiplier, 3)
        self.assertEqual(board.grid[13][5].multiplier, 3)
        self.assertEqual(board.grid[13][9].multiplier, 3)
        self.assertEqual(board.grid[0][3].multiplier, 2)
        self.assertEqual(board.grid[0][11].multiplier, 2)
        self.assertEqual(board.grid[2][6].multiplier, 2)
        self.assertEqual(board.grid[2][8].multiplier, 2)
        self.assertEqual(board.grid[3][0].multiplier, 2)
        self.assertEqual(board.grid[3][7].multiplier, 2)
        self.assertEqual(board.grid[3][14].multiplier, 2)
        self.assertEqual(board.grid[6][2].multiplier, 2)
        self.assertEqual(board.grid[6][6].multiplier, 2)
        self.assertEqual(board.grid[6][8].multiplier, 2)
        self.assertEqual(board.grid[6][12].multiplier, 2)
        self.assertEqual(board.grid[7][3].multiplier, 2)
        self.assertEqual(board.grid[7][11].multiplier, 2)
        self.assertEqual(board.grid[8][2].multiplier, 2)
        self.assertEqual(board.grid[8][6].multiplier, 2)
        self.assertEqual(board.grid[8][8].multiplier, 2)
        self.assertEqual(board.grid[8][12].multiplier, 2)
        self.assertEqual(board.grid[11][0].multiplier, 2)
        self.assertEqual(board.grid[11][7].multiplier, 2)
        self.assertEqual(board.grid[11][14].multiplier, 2)
        self.assertEqual(board.grid[12][6].multiplier, 2)
        self.assertEqual(board.grid[12][8].multiplier, 2)
        self.assertEqual(board.grid[14][3].multiplier, 2)
        self.assertEqual(board.grid[14][11].multiplier, 2)

    def test_word_inside_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        
        self.assertEqual(word_is_valid, True)
    
    def test_word_out_of_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
   
    def test_word_out_of_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
   
    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty(), True)
    
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7] = Tile('C', 1)
        self.assertEqual(board.is_empty(), False)
    
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_empty_board_vertical_wrong(self):
        board= Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (4, 2)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_no_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_no_empty_board_horizontal_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 3)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_no_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (4, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_no_empty_board_vertical_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (3, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_validate_word_horizontal_found_letter(self):    ### ESTE TEST NO ES SEGURO POR COMPLETO, PERO FUNCIONA XD ###
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        board.grid[7][4].add_letter(Tile('F', 1))  
        word_is_valid = board.validate_word_horizontal(word, location, orientation)
        self.assertEqual(word_is_valid, False)

    def test_place_word_no_empthy_2_coincidence_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[8][8].add_letter(Tile('L',1))
        board.grid[9][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (7,5)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_no_empthy_2_coincidence_horizontal_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        board.grid[7][8].add_letter(Tile('M',1))
        board.grid[8][8].add_letter(Tile('A',1))
        board.grid[9][8].add_letter(Tile('L',1))
        word = "Foca"
        location = (7,5)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_no_empthy_2_coincidence_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        board.grid[8][6].add_letter(Tile('A',1))
        board.grid[8][7].add_letter(Tile('L',1))
        board.grid[8][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (5,7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_no_empthy_2_coincidence_vertical_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        board.grid[8][7].add_letter(Tile('M',1))
        board.grid[8][8].add_letter(Tile('A',1))
        board.grid[8][9].add_letter(Tile('L',1))
        word = "Foca"
        location = (5,7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    ###TEST DE PALABRAS EN V Y EN H
    def check_word_insertion(self, board, word, location, orientation):
        board.insert(word, location, orientation)
        self.assertEqual(board.grid[location[0]][location[1]].letter.letter, word[0])
        for i in range(1, len(word)):
            if orientation == "H":
                self.assertEqual(board.grid[location[0]][location[1] + i].letter.letter, word[i])
            else:
                self.assertEqual(board.grid[location[0] + i][location[1]].letter.letter, word[i])

    def test_insert_horizontal(self):
        board = Board()
        word = "VENENO"
        location = (8, 8)
        orientation = "H"
        self.check_word_insertion(board, word, location, orientation)

    def test_insert_vertical(self):
        board = Board()
        word = "VENENO"
        location = (8, 8)
        orientation = "V"
        self.check_word_insertion(board, word, location, orientation)
    ###
    def test_converter_word_special_CHOCOLATE(self):
        board = Board()
        list_tiles = board.board_string_to_tiles("CHOCOLATE")
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
        board = Board()
        list_tiles = board.board_string_to_tiles("LLANTO")
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
        board = Board()
        list_tiles = board.board_string_to_tiles("TARRO")
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
        board = Board()  
        result = board.board_string_to_tiles("PYTHON")
        self.assertEqual([tile.letter for tile in result], [tile.letter for tile in expected_tiles])
        self.assertEqual([tile.value for tile in result], [tile.value for tile in expected_tiles])


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,5)
    def test_with_letter_multiplayer(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,7)

    def test_with_word_multiplayer(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,10)
    def test_with_word_and_letter_multiplayer(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,14)
    def test_with_word_and_letter_multiplayer_no_active(self):
        board = Board()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value,5)
if __name__ == '__main__':
    unittest.main()