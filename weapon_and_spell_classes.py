class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return "{} weapon with {} damage".format(self.name, self.damage)

    def __repr__(self):
        return "Weapon('{}', {})".format(self.name, self.damage)


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __str__(self):
        return "{} spell with {} damage, {} mana cost and {} cast range".format(self.name, self.damage, self.mana_cost, self.cast_range)

    def __repr__(self):
        return "Spell('{}', {}, {}, {})".format(self.name, self.damage, self.mana_cost, self.cast_range)
