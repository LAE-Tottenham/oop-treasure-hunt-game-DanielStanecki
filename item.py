class Item():
    def __init__(self, name):
        self.name = name
        
class Weapon(Item): 
    def __init__(self, name, dmg): 
        super().__init__(name)
        self.weaponDMG = dmg

    def setPlayerDMG(self, player): 
        player.DMG += self.weaponDMG
