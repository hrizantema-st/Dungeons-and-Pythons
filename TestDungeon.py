import unittest
from Dungeon import Dungeon
from Hero import Hero
from Dungeon import NotAHero

class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.my_hero = Hero("Bron","Dragonslayer", 100, 50, 2)
        self.my_dungeon = Dungeon(self.my_hero)

    def test_initialisation(self):
        self.assertTrue(isinstance(self.my_dungeon, Dungeon))

    def test_map_reading(self):
        needed = [['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
                  ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
                  ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
                  ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
                  ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(self.my_dungeon.map_reading("game_map.txt"), needed)

    def test_print_map(self):
        pass

    def test_spawn(self):
        with self.assertRaises(NotAHero):
            self.my_dungeon.spawn(10)
        self.my_dungeon.map_reading("game_map.txt")
        self.assertTrue(self.my_dungeon.spawn(self.my_hero))
        self.assertEqual(self.my_dungeon.hero_position_x, 0)
        self.assertEqual(self.my_dungeon.hero_position_y, 0)

    def test_move_hero_falses(self):
        self.my_dungeon.map_reading("game_map.txt")
        self.my_dungeon.spawn(self.my_hero)
        self.assertFalse(self.my_dungeon.move_hero("up"))
        self.assertFalse(self.my_dungeon.move_hero("left"))
        self.my_dungeon.hero_position_x = 4
        self.my_dungeon.hero_position_y = 9
        self.assertFalse(self.my_dungeon.move_hero("down"))
        self.assertFalse(self.my_dungeon.move_hero("right"))

    def test_move_hero(self):
        self.my_dungeon.map_reading("game_map.txt")
        self.my_dungeon.hero_position_x = 0
        self.my_dungeon.hero_position_y = 0
        self.assertTrue(self.my_dungeon.move_hero("right"))
        self.my_dungeon.hero_position_y = 2
        self.assertTrue(self.my_dungeon.move_hero("left"))
        self.my_dungeon.hero_position_x = 1
        self.my_dungeon.hero_position_y = 1
        self.assertTrue(self.my_dungeon.move_hero("up"))
        self.my_dungeon.hero_position_x = 1
        self.assertTrue(self.my_dungeon.move_hero("down"))

    def test_pick_treasure(self):
        pass


if __name__ == '__main__':
    unittest.main()
