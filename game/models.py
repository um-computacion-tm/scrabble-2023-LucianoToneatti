import random
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 11),
            Tile('B', 2),
            Tile('C', 4),
            Tile('D', 5),
            Tile('E', 11),
            Tile('F', 1),
            Tile('G', 2),
            Tile('H', 2),
            Tile('I', 6),
            Tile('J', 1),
            Tile('L', 4),
            Tile('M', 2),
            Tile('N', 5),
            Tile('Ñ', 1),
            Tile('O', 9),
            Tile('P', 2),
            Tile('Q', 1),
            Tile('R', 5),
            Tile('S', 6),
            Tile('T', 4),
            Tile('U', 5),
            Tile('V', 1),
            Tile('X', 1),
            Tile('Y', 1),
            Tile('Z', 1),
            Tile('?', 2)
        ]
        
        #Añadí las fichas de las letras restantes para llegar a 100
        remaining_tiles = 100 - len(self.tiles)
        for _ in range(remaining_tiles):
            self.tiles.append(Tile('?',0))
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles = self.tiles.pop(0)
        return tiles
    def put(self, tiles):
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)
        
    def initial_tiles(self):
        total = []
        initial_tiles = {'A':11,'B':2,'C':4,'D':5,'E':11,'F':1,
                         'G':2,'H':2,'I':6,'J':1,'L':4,'M':2,
                         'N':5,'O':9,'P':2,'Q':1,'R':5,'S':6,
                         'T':4,'U':5,'V':1,'X':1,'Y':1,'Z':1,'?':2}    
        for letter, amount in initial_tiles.items():
            matching_tiles = [tile for tile in self.tiles if tile.letter == letter]
            available_count = min(len(matching_tiles), amount)
            total.extend(matching_tiles[:available_count])    
        self.tiles.extend(total)