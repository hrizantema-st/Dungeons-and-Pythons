import unittest
from player import Player

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
        no_mana_player = Player (10, 0)
        self.assertFalse(no_mana_player.can_cast())

    def test_get_health(self):
        self.assertEqual(self.my_player.health, self.my_player.get_health())

    def test_get_mana(self):
        self.assertEqual(self.my_player.mana, self.my_player.get_mana())

    def test_healing(self):
        dead_player = Player(0, 12)
        self.assertFalse(dead_player.take_healing(2))
        self.my_player.health-=15
        self.assertTrue(self.my_player.take_healing(5))
        self.assertEqual(self.my_player.health, 25)

if __name__ == "__main__":
    unittest.main()
