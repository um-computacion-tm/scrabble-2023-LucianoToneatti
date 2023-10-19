from game.models import BagTiles
from game.models import Tile

class Several():

    def string_to_tiles(self, input_string, list):
        bag = BagTiles()
        letter_set = set(tile.letter for tile in bag.tiles)
        for letter in input_string.upper():
            if letter in letter_set:
                matching_tile = next(tile for tile in bag.tiles if tile.letter == letter)
                list.append(matching_tile)

    def board_string_to_tiles(self, input_string):
        bag = BagTiles()
        tiles_list = []
        special_letters = {"RR": 8, "LL": 8, "CH": 5}
        i = 0
        while i < len(input_string):
            letter = input_string[i]
            if i < len(input_string) - 1 and input_string[i:i+2] in special_letters:
                special_letter = input_string[i:i+2]
                tiles_list.append(Tile(letter=special_letter, value=special_letters[special_letter]))
                i += 2
            else:
                tiles_list.append(next(tile for tile in bag.tiles if tile.letter == letter.upper()))
                i += 1
        return tiles_list

    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'
    
    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'
    
    def is_desactive_or_none_multiplier(self,cell):
        return cell.status == 'desactive' or cell.multiplier_type == ''

    def calculate_word_value(self,word):
        total_value = 0
        word_multiplier = 1
        for cell in word:
            if self.is_desactive_or_none_multiplier(cell):
                total_value += cell.letter.value
            elif self.is_active_and_letter_multiplier(cell):
                total_value += cell.calculate_value()
            elif self.is_active_and_word_multiplier(cell):
                total_value += cell.calculate_value()
                word_multiplier *= cell.multiplier
        total_value *= word_multiplier
        return total_value
    
    def compare_tiles_and_letters(self, tile, word):
        if tile is not None:
            if tile.letter.lower() == word:
                return 1
            else:
                return 0
        else:
            return