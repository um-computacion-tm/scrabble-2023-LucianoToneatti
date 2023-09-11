import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 11)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 11)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self,patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),100)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.tiles)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.tiles), 98)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), 102)

    def test_initial_tiles(self):
        bag = BagTiles()
        bag.initial_tiles()
        self.assertEqual(len(bag.tiles),126)

if __name__ == '__main__':
    unittest.main()