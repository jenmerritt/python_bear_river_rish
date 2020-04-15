import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from fish import *

class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish1 = Fish("Salmon")
    
    def test_fish_has_name(self):
        self.assertEqual("Salmon", self.fish1.get_name())


if __name__ == "__main__":
    unittest.main() 