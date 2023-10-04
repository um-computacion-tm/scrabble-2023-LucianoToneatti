#test_player.py
import unittest
from game.player import Player
from game.models import BagTiles, Tile

"""class TestPlayer(unittest.TestCase):
    def test_player(self):
        player1 = Player()
        self.assertEqual(player1.rack,[])
    
    def test_player_get_tile(self):
        bag1 = BagTiles()
        player = Player()
        player.get_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    def test_player_exchange(self):
        bag1 = BagTiles()
        player = Player()
        player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        player.exchange_tiles(2,bag1)
        self.assertEqual(len(player.rack),3)
        self.assertEqual(len(bag1.tiles),29)  """

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.contains_letters(tiles)

        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.contains_letters(tiles)

        self.assertEqual(is_valid, False)

    def test_validate_fail_when_bag_tiles_is_none(self):
        player = Player() 
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
        ]
        is_valid = player.contains_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()