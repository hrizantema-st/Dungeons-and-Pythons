class Player:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self._maximum_health = health
        self._maximum_mana = mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, health):
        if not self.is_alive():
            return False

        self.health += health
        if self.health > self._maximum_health:
            self.health = self._maximum_health
        return True


