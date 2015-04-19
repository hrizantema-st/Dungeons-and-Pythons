from player import Player

class Hero(Player):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_mana(self, mana_points):
        self.mana += mana_points
        if self.mana > self._maximum_mana:
            self.mana = self._maximum_mana
        return True

    def attack(self, by):
        if by == "weapon":
            if self.weapon != []:
                return self.weapon[0].damage
            else:
                return 0
        if by == "spell":
            if self.spell != []:
                return self.spell[0].damage
            else:
                return 0
        else:
            raise ValueError
