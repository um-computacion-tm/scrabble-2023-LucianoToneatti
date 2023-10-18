from game.board import Board
from game.player import Player
from game.models import BagTiles
import uuid

class Scrabble:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.gameid = str(uuid.uuid4())
        for _ in range(players_count):
            self.players.append(Player())
        self.current_player = None
        self.turn = 1
        self.grid = [[' ' for _ in range(15)] for _ in range(15)] 

    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            player_turn = self.players.index(self.current_player) + 1
            self.current_player = self.players[player_turn]
        self.turn += 1

    def scrabble_validate_word(self, word, location, orientation):
        return self.board.validate_word_inside_board(word, location, orientation)
   
    def scrabble_word_calculate_score(self, word):
        total_score = 0
        for cell in word:
            tile = cell.letter
            tile_value = tile.value
            cell_multiplier = cell.multiplier
            total_score += tile_value * cell_multiplier
        self.current_player.score += total_score
