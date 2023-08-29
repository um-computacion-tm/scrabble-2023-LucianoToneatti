from game.models import BagTiles
from game.models import Tile

class Player:
    def __init__(self):
        self.bag = BagTiles()
        self.tiles = self.bag.take(7)
    def score(self):
        pass
    def exchange(self, tile_index):
        if 0 <= tile_index < len(self.tiles):
            exchanged_tile = self.tiles.pop(tile_index)
            self.bag.put([exchanged_tile])
            new_tile = self.bag.take(1)[0]
            self.tiles.append(new_tile)
    def __str__(self):
        return ', '.join(tile.letter for tile in self.tiles)  
        

