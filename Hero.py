from player import Player
from weapon_and_spell_classes import Weapon
from weapon_and_spell_classes import Spell

class Hero(Player):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = []
        self.spell = []

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_mana(self, mana_points):
        self.mana += mana_points
        if self.mana > self._maximum_mana:
            self.mana = self._maximum_mana
        return True

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

    def attack(self, by):
        if by == "weapon":
            if self.weapon != []:
                return self.weapon[0].damage
        if by == "spell":
            if self.spell != []:
                return self.spell[0].damage
        else:
            raise ValueError
