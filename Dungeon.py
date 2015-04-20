from Hero import Hero
from random import randint
import json
from weapon_and_spell_classes import Spell
from weapon_and_spell_classes import Weapon


class NotAHero(Exception):
    pass


class Dungeon:

    @staticmethod
    def map_reading(path):
        text_file = open(path, "r")
        text = text_file.read().split('\n')
        text_file.close()
        my_map = text[:-1]
        my_map = [list(l) for l in my_map]
        return my_map

    def __init__(self, hero, my_map):
        self.list = Dungeon.map_reading("game_map.txt")
        self.hero_position_x = -1
        self.hero_position_y = -1
        self.hero = hero

    def print_map(self):
        for l in self.list:
            return ("".join(l))

    def spawn(self, hero):
        if not (isinstance(hero, Hero)):
            raise NotAHero
        for l in range(0, len(self.list)):
            for x in range(0, len(self.list[l])):
                if self.list[l][x] == 'S':
                    self.list[l][x] = 'H'
                    self.hero_position_x = l
                    self.hero_position_y = x
                    return True

    def move_hero(self, direction):
        if direction == "up":
            if self.hero_position_x == 0:
                return False
            next_x_position = self.hero_position_x - 1
            next_y_position = self.hero_position_y

        if direction == "down":
            if self.hero_position_x == len(self.list) - 1:
                return False
            next_x_position = self.hero_position_x + 1
            next_y_position = self.hero_position_y

        if direction == "left":
            if self.hero_position_y == 0:
                return False
            next_y_position = self.hero_position_y - 1
            next_x_position = self.hero_position_x

        if direction == "right":
            if self.hero_position_y == len(self.list[0]) - 1:
                return False
            next_x_position = self.hero_position_x
            next_y_position = self.hero_position_y + 1

        if self.list[next_x_position][next_y_position] == "#":
            return False
        else:
            if self.list[next_x_position][next_y_position] == "E":
                self.hero.take_mana(self.hero.mana_regeneration_rate)
                self.changing_pos_func(next_x_position, next_y_position)
                pass
            if self.list[next_x_position][next_y_position] == "T":
                self.hero.take_mana(self.hero.mana_regeneration_rate)
                self.changing_pos_func(next_x_position, next_y_position)
                self.pick_treasure("treasures.json")
            if self.list[next_x_position][next_y_position] == ".":
                self.changing_pos_func(next_x_position, next_y_position)
                self.hero.take_mana(self.hero.mana_regeneration_rate)
            if self.list[next_x_position][next_y_position] == "G":
                self.changing_pos_func(next_x_position, next_y_position)
                print("This is the Gate to an other Dungeon")
            return True

    def changing_pos_func(self, x, y):
        self.list[x][y] = 'H'
        self.list[self.hero_position_x][self.hero_position_y] = '.'
        self.hero_position_x = x
        self.hero_position_y = y

    @staticmethod
    def load_treasure_file(path):
        with open(path, 'r') as load_file:
            load_data = load_file.read()
            my_treasure = json.loads(load_data)
        return my_treasure

    def pick_treasure(self, my_treasure):
        for key in my_treasure:
            my_treasure_type = key
            x = len(my_treasure[my_treasure_type])
            tr = my_treasure[my_treasure_type][randint(0, x - 1)]
        if my_treasure_type == 'mana':
            self.hero.take_mana(tr)
            return "{}'s treasure are {} mana points".format(self.hero.name, tr)
        elif my_treasure_type == 'health':
            self.hero.take_healing(tr)
            return "{}'s treasure are {} health points".format(self.hero.name, tr)
        elif my_treasure_type == 'spell':
            this_spell = eval(my_treasure[my_treasure_type][
                randint(0, len(my_treasure[my_treasure_type]) - 1)])
            self.hero.learn(this_spell)
            return "{}'s treasure is {}".format(self.hero.name, this_spell)
        else:
            this_weapon = eval(my_treasure[my_treasure_type][
                randint(0, len(my_treasure[my_treasure_type]) - 1)])
            self.hero.equip(this_weapon)
            return "{}'s treasure is {}".format(self.hero.name, this_weapon)
