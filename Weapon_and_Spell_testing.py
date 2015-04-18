import unittest
from weapon_and_spell_classes import Weapon
from weapon_and_spell_classes import Spell

class TestWeapon(unittest.TestCase):

    def test_initialisation(self):
        w = Weapon("Hammer", 10)
        self.assertTrue(isinstance(w, Weapon))

class TestSpell(unittest.TestCase):

    def test_init(self):
        s = Spell("Potion", 20, 25, 1)
        self.assertTrue(isinstance(s, Spell))

if __name__ == "__main__":
    unittest.main()
