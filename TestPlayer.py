import unittest
from player import Player
from weapon_and_spell_classes import Weapon
from weapon_and_spell_classes import Spell


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.my_player = Player(35, 20)

    def test_initialisation(self):
        self.assertTrue(isinstance(self.my_player, Player))

    def test_is_alive(self):
        dead_player = Player(0, 12)
        self.assertFalse(dead_player.is_alive())
        self.assertTrue(self.my_player.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.my_player.can_cast())
        no_mana_player = Player(10, 0)
        self.assertFalse(no_mana_player.can_cast())

    def test_get_health(self):
        self.assertEqual(self.my_player.health, self.my_player.get_health())

    def test_get_mana(self):
        self.assertEqual(self.my_player.mana, self.my_player.get_mana())

    def test_healing(self):
        dead_player = Player(0, 12)
        self.assertFalse(dead_player.take_healing(2))
        self.my_player.health -= 15
        self.assertTrue(self.my_player.take_healing(5))
        self.assertEqual(self.my_player.health, 25)

    def test_learn(self):
        s = Spell("Potion", 20, 25, 1)
        self.my_player.learn(s)
        self.assertEqual(self.my_player.spell, [s])
        s1 = Spell("Fireball", 30, 50, 2)
        self.my_player.learn(s1)
        self.assertEqual(self.my_player.spell, [s1])

    def test_equip(self):
        w = Weapon("Hammer", 10)
        self.my_player.equip(w)
        self.assertEqual(self.my_player.weapon, [w])
        w1 = Weapon("Sword", 35)
        self.my_player.equip(w1)
        self.assertEqual(self.my_player.weapon, [w1])

    def test_take_damage(self):
        self.my_player.take_damage(30)
        self.assertEqual(self.my_player.health, 5)
        self.my_player.take_damage(15)
        self.assertEqual(self.my_player.health, 0)

    def test_take_mana(self):
        pass

    def test_attack(self):
        pass

if __name__ == "__main__":
    unittest.main()
