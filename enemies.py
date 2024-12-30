import random

class Enemy(): 
    def __init__(self, name, dmg, hp): 
        self.name = name
        self.dmg = dmg
        self.hp = hp
    
    def attack(self, player): 
        dmgRoll = random.randrange(1, 21)
        if dmgRoll > 10: 
            player.health -= (dmgRoll - 10) * self.dmg
        elif dmgRoll < 10: 
            player.health -= self.dmg // (10 - dmgRoll)
        elif dmgRoll == 10:
            player.health -= self.dmg

    def viewStats(self): 
        print(f"{self.name} Health: {self.hp}")

class Boss(Enemy): 
    def __init__(self, name, dmg, hp, special): 
        super().__init__(name, dmg, hp)
        self.special = special