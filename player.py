class Player:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self._maximum_health = health
        self._maximum_mana = mana
        self.weapon = []
        self.spell = []

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

    def take_mana():
        pass

    def learn(self, spell):
        if self.spell == []:
            self.spell.append(spell)
        else:
            if self.spell[0].damage < spell.damage:
                self.spell[0] = spell
            else:
                pass

    def equip(self, weapon):
        if self.weapon == []:
            self.weapon.append(weapon)
        else:
            if self.weapon[0].damage < weapon.damage:
                self.weapon[0] = weapon
            else:
                pass

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def attack(self, by):
        pass
