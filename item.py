class Item():
    def __init__(self, name):
        self.name = name
        self.type = None
        
class Weapon(Item): 
    def __init__(self, name, dmg): 
        super().__init__(name)
        self.weaponDMG = dmg

    def setPlayerDMG(self, player): 
        player.damage += self.weaponDMG


#test:

"""class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.maxHealth = 100
        self.maxEnergy = 100
        self.health = 100
        self.energy = 100
        self.inventoryMax = 12
        self.inventory = []
        self.damage = 2
        
    def calculateInventory_size(self):
             return len.self.inventory + 1

    def addItem(self, item_instance):
        if self.calculate_inventory_size() > self.inventoryMax:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def removeItem(self): 
        print(self.inventory)
        input = input("Please choose an item to remove")
        
    def viewStats(self): 
        print(f"Health: {self.health}           Energy: {self.energy}")

    def useItem(self, item):
        if item.name == "Stamina Potion":
            if self.energy >= self.maxEnergy - 50:
                self.energy = self.maxEnergy
            else:  
                self.energy += 50
        elif item.name == "HP Potion":
            if self.health >= self.maxHealth - 50: 
                self.health = self.maxHealth
            else: 
                self.health += 50"""
       
"""daniel = Player("Daniel")
hpPotion = Item("HP Potion")
energyPotion = Item("Stamina Potion")
daniel.useItem(hpPotion)
daniel.useItem(energyPotion)
daniel.viewStats()"""