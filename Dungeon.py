class Dungeon:

    def __init__(self):
        self.list = []

    def map_reading(self, path):
        text_file = open(path, "r")
        text = text_file.read().split('\n')
        text_file.close()
        self.list = text[:-1]
        self.list = [list(l) for l in self.list]
        return self.list

a = Dungeon()
print(a.map_reading('game_map.txt'))
