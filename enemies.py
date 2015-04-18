from player import Player

class Enemy(Player):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage

    def take_mana():
        pass

    def attack(self, by = ""):
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
        if by =="":
            return self.damage
        else:
            raise ValueError
