from Hero import Hero
from random import randint
import json
from weapon_and_spell_classes import Spell
from weapon_and_spell_classes import Weapon


class NotAHero(Exception):
    pass


class IncorrectDirection(Exception):
    pass


class Dungeon:

    OBSTACLE = "#"
    SPAWNING_POINT = "S"
    ENEMY = "E"
    EXIT = "G"
    tREASURE = "T"
    WALKABLE_PATH = "."
    HERO = "H"

    DIRECTIONS = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }

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
                if self.list[l][x] == Dungeon.SPAWNING_POINT:
                    self.list[l][x] = Dungeon.HERO
                    self.hero_position_x = l
                    self.hero_position_y = x
                    return True

    def move_hero(self, direction):

        if direction not in Dungeon.DIRECTIONS
            raise IncorrectDirection

        next_x_position = self.hero_position_x + Dungeon.DIRECTIONS[direction][0]
        next_y_position = self.hero_position_y + Dungeon.DIRECTIONS[direction][1]

        if next_x_position not in range(0, len(self.list)) \
                or next_y_position in [-1, len(self.list[0])]:
            return False

        if self.list[next_x_position][next_y_position] == Dungeon.OBSTACLE:
            return False
        else:
            if self.list[next_x_position][next_y_position] == Dungeon.ENEMY:
                pass
            elif self.list[next_x_position][next_y_position] == Dungeon.TREASURE:
                self.pick_treasure("treasures.json")
            elif self.list[next_x_position][next_y_position] == Dungeon.EXIT:
                print("This is the Gate to an other Dungeon")
            else:
                pass  # SPAWNING_POINT or WALKABLE_PATH

            self.hero.take_mana(self.hero.mana_regeneration_rate)
            self.changing_pos_func(next_x_position, next_y_position)
            return True

    def changing_pos_func(self, x, y):
        self.list[x][y] = Dungeon.HERO
        self.list[self.hero_position_x][self.hero_position_y] = Dungeon.WALKABLE_PATH
        self.hero_position_x = x
        self.hero_position_y = y

    def pick_treasure(self, path):
        with open(path, 'r') as load_file:
            load_data = load_file.read()
            my_treasure = json.loads(load_data)
            for key in my_treasure:
                my_treasure_type = key
            if my_treasure_type == 'mana':
                x = len(my_treasure[my_treasure_type])
                tr = my_treasure[my_treasure_type][randint(0, x - 1)]
                self.hero.take_mana(tr)
                return "{}'s treasure are {} mana points".format(self.hero.name, tr)
            elif my_treasure_type == 'health':
                x = len(my_treasure[my_treasure_type])
                tr = my_treasure[my_treasure_type][randint(0, x - 1)]
                self.hero.take_healing(tr)
                return "{}'s treasure are {} health points".format(self.hero.name, tr)
            elif my_treasure_type == 'spell':
                this_spell = my_treasure[my_treasure_type][
                    randint(0, len(my_treasure[my_treasure_type]) - 1)]
                s = Spell(
                    this_spell[0], this_spell[1], this_spell[2], this_spell[3])
                self.hero.learn(s)
                return "{}'s treasure is {}".format(self.hero.name, s)
            else:
                this_weapon = my_treasure[my_treasure_type][
                    randint(0, len(my_treasure[my_treasure_type]) - 1)]
                w = Weapon(this_weapon[0], this_weapon[1])
                self.hero.equip(w)
                return "{}'s treasure is {}".format(self.hero.name, w)
