import random

class Item():
    def __init__(self, name):
        self.name = name
        self.type = None
        
class Weapon(Item): 
    def __init__(self, name, dmg): 
        super().__init__(name)
        self.weaponDMG = dmg

class Buff(Item): 
    def __init__(self, name): 
        super().__init__(name)

    def buffPlayer(self, player):  
        player.baseDamage += 1
        player.damage = player.baseDamage + player.weaponDamage
        player.maxHealth += 25
        player.energy += 10
        player.health = player.maxHealth
        

#test:

