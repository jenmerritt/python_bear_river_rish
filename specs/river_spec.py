import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from river import *
from fish import *

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.empty_river = []
        self.amazon = River("Amazon", self.empty_river)
        self.salmon = Fish("Salmon")
        self.trout = Fish("Trout")
        self.stocked_river = River("Blue River", [self.salmon, self.trout, self.salmon, self.trout, self.salmon, self.trout])

    def test_river_has_name(self):
        self.assertEqual("Amazon", self.amazon.get_name())
    
    def test_scope_name(self):
        new_river = River("Ouse", [self.trout])
        new_river.add_fish(self.trout)
        self.assertEqual("Ouse", new_river.get_name())
        self.assertEqual(2, new_river.get_number_of_fish())
    
    def test_default_fish_empty_list(self):
        self.assertEqual(0, self.amazon.get_number_of_fish())
    
    def test_can_get_number_of_fish(self):
        self.assertEqual(6, self.stocked_river.get_number_of_fish())
    
    def test_can_add_fish_to_river(self):
        river = River("Missippi", self.empty_river)
        fish = Fish("Salmon")
        river.add_fish(fish)
        river.add_fish(fish)
        river.add_fish(fish)
        self.assertEqual(3, river.get_number_of_fish())
    
    def test_can_yield_fish(self):
        yielded_fish = self.stocked_river.yield_fish()
        self.assertEqual(self.trout, yielded_fish)
    
    def test_cannot_yield_fish_if_empty(self):
        self.assertIsNone(self.amazon.yield_fish())


if __name__ == "__main__":
    unittest.main() 