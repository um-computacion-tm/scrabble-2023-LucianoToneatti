from game.models import BagTiles
#player.py
class Player:
    """def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)  """

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