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

    def move_hero(self, direction):
    if direction == "up":
        if self.hero_position_y == 0:
            return False
        next_x_position = self.hero_position_x
        next_y_position = self.hero_position_y - 1

    if direction == "down":
        if self.hero_position_y == len(self.list) - 1:
            return False
        next_x_position = self.hero_position_x
        next_y_position = self.hero_position_y + 1

    if direction == "left":
        if self.hero_position_x == 0:
            return False
        next_y_position = self.hero_position_y
        next_x_position = self.hero_position_x - 1

    if direction == "right":
        if self.hero_position_x == len(self.list[1]) - 1:
            return False
        next_x_position = self.hero_position_x + 1
        next_y_position = self.hero_position_y

        if self.list[next_x_position][next_y_position] == "#":
            return False
        if self.list[next_x_position][next_y_position] == "E":
            pass # start a fight
        if self.list[next_x_position][next_y_position] == "T":
            pass
        if self.list[next_x_position][next_y_position] == ".":
            self.hero_position_x = next_x_position
            self.hero_position_y = next_y_position
            return True


a = Dungeon()
print(a.map_reading('game_map.txt'))


