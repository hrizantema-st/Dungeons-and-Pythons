from enemies import Enemy
import unittest


class TestingEnemies(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(100, 100, 20)
        self.dead_enemy = Enemy(0, 0, 10)

    def test_init(self):
        self.assertTrue(isinstance(self.enemy, Enemy))

    def test_is_alive(self):
        self.assertEqual(self.enemy.is_alive(), True)
        self.assertFalse(self.dead_enemy.is_alive())

    def test_can_cast(self):
        self.assertEqual(self.enemy.can_cast(), True)
        self.assertFalse(self.dead_enemy.can_cast())

    def test_get_health(self):
        self.assertTrue(self.enemy.get_health(), 100)
        self.assertFalse(self.dead_enemy.get_health(), 100)

    def test_get_mana(self):
        self.assertTrue(self.enemy.get_mana())

    def test_take_healing(self):
        self.assertTrue(self.enemy.take_healing(10))
        self.assertFalse(self.dead_enemy.take_healing(20))

if __name__ == '__main__':
    unittest.main()
