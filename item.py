class Item():
    def __init__(self, name):
        self.name = name
        
class Weapon(Item): 
    def __init__(self, name, dmg): 
        super().__init__(name)
        self.weaponDMG = dmg

    def setPlayerDMG(self, player): 
        player.DMG += self.weaponDMG

class HpPotion(Item): 
    def __init__(self, name, heal): 
        super().__init__(name)
        self.heal = heal

class StaminaPotion(Item): 
    def __init__(self, name, heal): 
        super().__init__(name)
        self.heal = heal

#/ class Test(): 
    def __init__(self, DMG): 
        self.DMG = DMG
    
    def sum(self): 
        print(self.DMG) 
#/
