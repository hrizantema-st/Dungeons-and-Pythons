import unittest
from weapon_and_spell_classes import Weapon
from weapon_and_spell_classes import Spell


class TestWeapon(unittest.TestCase):

    def test_initialisation(self):
        w = Weapon("Hammer", 10)
        self.assertTrue(isinstance(w, Weapon))

    def test_str(self):
        w = Weapon("Hammer", 10)
        needed = "Hammer weapon with 10 damage"
        self.assertEqual(needed, w.__str__())

    def test_repr(self):
        w = Weapon("Hammer", 10)
        needed = "Weapon('Hammer', 10)"
        self.assertEqual(needed, w.__repr__())


class TestSpell(unittest.TestCase):

    def test_init(self):
        s = Spell("Potion", 20, 25, 1)
        self.assertTrue(isinstance(s, Spell))

    def test_str(self):
        s = Spell("Potion", 20, 25, 1)
        needed = "Potion spell with 20 damage, 25 mana cost and 1 cast range"
        self.assertEqual(needed, s.__str__())

    def test_repr(self):
        s = Spell("Potion", 20, 25, 1)
        needed = "Spell('Potion', 20, 25, 1)"
        self.assertEqual(needed, s.__repr__())

if __name__ == "__main__":
    unittest.main()
