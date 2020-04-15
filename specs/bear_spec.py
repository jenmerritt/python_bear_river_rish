import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from bear import *
from fish import *
from river import *

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear = Bear("Baloo", "Sloth Bear")
        self.fish = Fish("Salmon")
        self.river = River("Amazon", [self.fish, self.fish, self.fish])
    
    def test_can_get_name(self):
        self.assertEqual("Baloo", self.bear.get_name())

    def test_can_get_breed(self):
        self.assertEqual("Sloth Bear", self.bear.get_breed())
    
    def test_stomach_starts_empty(self):
        self.assertEqual(0, self.bear.get_number_of_fish_in_stomach())
    
    def test_bear_can_roar(self):
        self.assertEqual("ROAR!", self.bear.roar())
    
    def test_bear_can_take_fish(self):
        self.bear.take_fish(self.river)
        self.bear.take_fish(self.river)
        self.assertEqual(2, self.bear.get_number_of_fish_in_stomach())
    
    def test_bear_cannot_take_fish_from_empty_river(self):
        self.bear.take_fish(self.river)
        self.bear.take_fish(self.river)
        self.bear.take_fish(self.river)
        self.bear.take_fish(self.river)
        self.assertEqual(3, self.bear.get_number_of_fish_in_stomach())

if __name__ == "__main__":
    unittest.main() 