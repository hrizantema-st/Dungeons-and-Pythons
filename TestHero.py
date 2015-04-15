import unittest
from Hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_initialisation(self):
        self.assertTrue(isinstance(self.h, Hero))

    def test_known_as(self):
        needed = "Bron the Dragonslayer"
        self.assertEqual(needed, self.h.known_as())

    def test_get_health(self):
        self.assertEqual(self.h.health, self.h.get_health())

    def test_is_alive(self):
        my_hero = Hero(
            name="Elena", title="Human", health=0, mana=10, mana_regeneration_rate=20)
        self.assertFalse(my_hero.is_alive())
        self.assertTrue(self.h.is_alive())

    def test_get_mana(self):
        self.assertEqual(self.h.mana, self.h.get_mana())

    def test_can_cast(self):
        self.assertTrue(self.h.can_cast())
        my_hero = Hero(
            name="Elena", title="Human", health=100, mana=0, mana_regeneration_rate=20)
        self.assertFalse(my_hero.can_cast())

    def test_take_damage(self):
        self.h.take_damage(2.2)
        self.assertEqual(self.h.health, 97.8)

    def test_healing(self):
        my_hero = Hero(
            name="Elena", title="Human", health=0, mana=10, mana_regeneration_rate=20)
        self.assertFalse(my_hero.take_healing(2))
        self.h.take_damage(12)
        self.assertTrue(self.h.take_healing(6))
        self.assertEqual(self.h.health, 94)


if __name__ == "__main__":
    unittest.main()
