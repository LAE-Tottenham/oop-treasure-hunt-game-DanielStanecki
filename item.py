import random

class Item():
    def __init__(self, name):
        self.name = name
        self.type = None
        
class Weapon(Item): 
    def __init__(self, name, dmg): 
        super().__init__(name)
        self.weaponDMG = dmg

    def setPlayerDMG(self, player): 
        player.damage = player.baseDamage + self.weaponDMG

class Buff(Item): 
    def __init__(self, name, buff, type): 
        super().__init__(name)
        self.buff = buff
        self.type = type

    def buffPlayer(self, player): 
        if self.type == "Damage": 
            

#test:
class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.maxHealth = 100
        self.maxEnergy = 100
        self.health = 100
        self.energy = 50
        self.inventoryMax = 12
        self.inventory = []
        self.baseDamage = 2
        self.damage = self.baseDamage
        self.money = 100
        
    def calculateInventory_size(self):
             return len(self.inventory) + 1

    def addItem(self, item_instance):
        if self.calculateInventory_size() < self.inventoryMax:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def playerRemoveItem(self): 
        print(self.inventory)
        item = input("Please choose an item to remove: ")
        self.inventory.remove(item)

    def viewStats(self): 
        print(f"Player Health: {self.health}           Energy: {self.energy}")
        
    def useItem(self, item):
        if item.name in self.inventory: 
            if item.name == "Stamina Potion":
                if self.energy >= self.maxEnergy - 50:
                    self.energy = self.maxEnergy
                else:  
                    self.energy += 50
            elif item.name == "HP Potion":
                if self.health >= self.maxHealth - 50: 
                    self.health = self.maxHealth
                else: 
                    self.health += 50
            self.inventory.remove(item.name)
        else: 
            print("You do not currently have this item in your inventory.")
    
    def attack(self, enemy): 
        dmgRoll = random.randrange(1, 21)
        if dmgRoll > 10: 
            enemy.hp -= (dmgRoll - 10) * self.damage
        elif dmgRoll < 10: 
            enemy.hp -= self.damage // (10 - dmgRoll)
        elif dmgRoll == 10:
            enemy.hp -= self.damage

damageBuff = Buff("Damage Buff", 5, "baseDamage")     
daniel = Player("Daniel")
sword = Weapon("Sword", 4)
sword.setPlayerDMG(daniel)
print(daniel.damage)
print(daniel.baseDamage)
mace = Weapon("Mace", 7)
mace.setPlayerDMG(daniel)
print(daniel.damage)
print(daniel.baseDamage)
damageBuff.buffPlayer(daniel)
