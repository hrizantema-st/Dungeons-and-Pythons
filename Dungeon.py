from Hero import Hero
from random import randint
import json
from weapon_and_spell_classes import Spell
from weapon_and_spell_classes import Weapon

class NotAHero(Exception):
    pass


class Dungeon:

    def __init__(self, hero):
        self.list = []
        self.hero_position_x = -1
        self.hero_position_y = -1
        self.hero = hero

    def map_reading(self, path):
        text_file = open(path, "r")
        text = text_file.read().split('\n')
        text_file.close()
        self.list = text[:-1]
        self.list = [list(l) for l in self.list]
        return self.list

    def print_map(self):
        for l in self.list:
            print("".join(l))

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
        if self.list[next_x_position][next_y_position] == "E":
            self.hero.take_mana(self.hero.mana_regeneration_rate)
            pass
        if self.list[next_x_position][next_y_position] == "T":
            self.hero.take_mana(self.hero.mana_regeneration_rate)
            pass
        if self.list[next_x_position][next_y_position] == ".":
            self.hero_position_x = next_x_position
            self.hero_position_y = next_y_position
            self.hero.take_mana(self.hero.mana_regeneration_rate)
            return True
        if self.list[next_x_position][next_y_position] == "G":
            pass



    def read_treasure_file(self, path):
         with open(path, 'r') as load_file:
            load_data = load_file.read()
            my_treasure = json.loads(load_data)
            for key in my_treasure:
                my_treasure_type = key
            if my_treasure_type == 'mana':
                x = len(my_treasure[my_treasure_type])
                self.hero.take_mana(my_treasure[my_treasure_type][randint(0, x - 1)])
            elif my_treasure_type == 'health':
                x = len(my_treasure[my_treasure_type])
                self.hero.take_healing(my_treasure[my_treasure_type][randint(0, x - 1)])
            elif my_treasure_type == 'spell':
                this_spell = my_treasure[my_treasure_type][randint(0,len(my_treasure[my_treasure_type]) - 1)]
                s = Spell(this_spell[0], this_spell[1], this_spell[2], this_spell[3])
                self.hero.learn(s)
            else:
                this_weapon = my_treasure[my_treasure_type][randint(0,len(my_treasure[my_treasure_type]) - 1)]
                w = Weapon(this_weapon[0], this_weapon[1])
                self.hero.equip(w)


my_hero = Hero("Bron", "Dragonslayer", 100, 100, 2)
a = Dungeon(my_hero)
a.map_reading('game_map.txt')
a.spawn(my_hero)
a.print_map()
a.hero_position_x
a.hero_position_y
a.move_hero("right")
print(a.read_treasure_file("treasures.json"))
