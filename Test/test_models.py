import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestBagTiles(unittest.TestCase):
    def test_tile_creation(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_bag_initialization(self):
        bag = BagTiles()
    def test_take_tiles(self):
        bag = BagTiles()
        initial_tiles_count = len(bag.tiles)
        taken_tiles = bag.take(7)
        self.assertEqual(len(taken_tiles), 7)
        self.assertEqual(len(bag.tiles), initial_tiles_count - 7)
    def test_put_tiles(self):
        bag = BagTiles()
        initial_tiles_count = len(bag.tiles)
        put_tiles = [Tile('X', 8), Tile('Q', 5)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), initial_tiles_count + 2)


if __name__ == '__main__':
    unittest.main()