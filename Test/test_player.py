import unittest
from game.player import Player
from game.models import BagTiles

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    
    def test_initial_tiles(self):
        self.assertEqual(len(self.player.tiles), 7)

    def test_exchange(self):
        initial_tiles = self.player.tiles.copy()
        initial_bag_size = len(self.player.bag.tiles)
        
        
        self.player.exchange(0)
        
        self.assertNotEqual(initial_tiles, self.player.tiles)
        self.assertEqual(len(self.player.tiles), 7)  
        self.assertEqual(len(self.player.bag.tiles), initial_bag_size)  



if __name__ == '__main__':
    unittest.main()
