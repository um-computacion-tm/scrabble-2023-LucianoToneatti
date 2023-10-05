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
    def scrabble_string_to_tiles(self, input_string):
        bag = BagTiles()
        return [tile for letter in input_string.upper() for tile in bag.tiles if tile.letter == letter]
