from player import Player

class Enemy(Player):

    def __init__(self, health, mana, damage):
        self._maximum_health = health
        self.health = health
        self._maximum_mana = mana
        self.mana = mana
        self.damage = damage

    def attack(self):
        pass
