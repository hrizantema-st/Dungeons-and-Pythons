class Enemy:

    def __init__(self, health, mana, damage):
        self._maximum_health = health
        self.health = health
        self._maximum_mana = mana
        self.mana = mana
        self.damage = damage

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

    def take_mana(self):
        pass

    def attack(self):
        pass
