from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

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
    def validate_word_inside_board(self,word, location, orientation):
        col = location[0]
        row = location[1]
        word_length = len(word)
        if orientation == "H":
            return col + word_length <= 15
        elif orientation == "V":
            return row + word_length <= 15
    
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
    def validate_word_place_board(self):
        pass