from enemies import Enemy
import unittest
from weapon_and_spell_classes import Weapon
from weapon_and_spell_classes import Spell


class TestingEnemies(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(100, 100, 20)
        self.dead_enemy = Enemy(0, 0, 10)

    def test_initialisation(self):
        self.assertIsInstance(self.enemy, Enemy)

    def test_attack(self):
        self.assertEqual(self.enemy.attack("weapon"), 0)
        self.assertEqual(self.enemy.attack("spell"), 0)
        self.assertEqual(self.enemy.attack(), 20)
        w = Weapon("Hammer", 10)
        self.enemy.equip(w)
        s = Spell("Potion", 20, 25, 1)
        self.enemy.learn(s)
        self.assertEqual(self.enemy.attack("weapon"), 10)
        self.assertEqual(self.enemy.attack("spell"), 20)
        with self.assertRaises(ValueError):
            self.enemy.attack("hammer")

if __name__ == '__main__':
    unittest.main()
