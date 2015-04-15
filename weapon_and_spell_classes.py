class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
