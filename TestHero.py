import unittest
from Hero import Hero
from weapon_and_spell_classes import Spell
from weapon_and_spell_classes import Weapon


class TestHero(unittest.TestCase):

    def setUp(self):
        self.h = Hero("Bron","Dragonslayer", 100, 50, 2)

    def test_initialisation(self):
        self.assertTrue(isinstance(self.h, Hero))

    def test_known_as(self):
        needed = "Bron the Dragonslayer"
        self.assertEqual(needed, self.h.known_as())

    def test_take_damage(self):
        self.h.take_damage(2.2)
        self.assertEqual(self.h.health, 97.8)

    def test_take_mana(self):
        self.assertTrue(self.h.take_mana(10))

    def test_learn(self):
        s = Spell("Potion", 20, 25, 1)
        self.h.learn(s)
        self.assertEqual(self.h.spell, [s])
        s1 = Spell("Fireball", 30, 50, 2)
        self.h.learn(s1)
        self.assertEqual(self.h.spell, [s1])

    def test_equip(self):
        w = Weapon("Hammer", 10)
        self.h.equip(w)
        self.assertEqual(self.h.weapon, [w])
        w1 = Weapon("Sword", 35)
        self.h.equip(w1)
        self.assertEqual(self.h.weapon, [w1])

    def test_attack(self):
        self.assertEqual(self.h.attack("weapon"), 0)
        self.assertEqual(self.h.attack("spell"), 0)
        w = Weapon("Hammer", 10)
        self.h.equip(w)
        s = Spell("Potion", 20, 25, 1)
        self.h.learn(s)
        self.assertEqual(self.h.attack("weapon"), 10)
        self.assertEqual(self.h.attack("spell"), 20)
        with self.assertRaises(ValueError):
            self.h.attack("hammer")

if __name__ == "__main__":
    unittest.main()
