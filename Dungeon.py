from Hero import Hero


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
        for l in self.list:
            for x in range(0, len(l)):
                if l[x] == 'S':
                    l[x] = 'H'
                    return True

a = Dungeon()
a.map_reading('game_map.txt')
my_hero = Hero("Bron", "Dragonslayer", 100, 100, 2)
print(a.spawn(my_hero))
a.print_map()
