from game.models import BagTiles
#player.py
class Player:

    def __init__(self, bag_tiles=None):
        self.tiles = []
        self.score = 0
        self.bag_tiles = bag_tiles

    def contains_letters(self, tiles):
        if not self.bag_tiles:
            return False
        available_tiles = [tile.letter for tile in self.bag_tiles.tiles]
        for tile in tiles:
            if tile.letter in available_tiles:
                available_tiles.remove(tile.letter)
            else:
                return False
        return True

    def display_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.rack)