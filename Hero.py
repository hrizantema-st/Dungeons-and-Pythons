from player import Player

class Hero(Player):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0
