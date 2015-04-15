class Hero:

    def __init__(self, name="", title="", health=100, mana=100, mana_regeneration_rate=0):
        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health != 0

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return self.mana != 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        else:
            self.health += healing_points
            if self.health > self.max_health:
                self.health = self.max_health
            return True

    def take_mana(self, mana_points):
    	pass
