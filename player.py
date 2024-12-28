import random

class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.maxHealth = 100
        self.maxEnergy = 100
        self.health = 5
        self.energy = 50
        self.inventoryMax = 12
        self.inventory = []
        self.damage = 2
        
    def calculateInventory_size(self):
             return len(self.inventory) + 1

    def addItem(self, item_instance):
        if self.calculateInventory_size() < self.inventoryMax:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def removeItem(self): 
        print(self.inventory)
        item = input("Please choose an item to remove: ")
        self.inventory.remove(item)

    def viewStats(self): 
        print(f"Player Health: {self.health}           Energy: {self.energy}")
        
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
                self.health += 50
    
    def attack(self, enemy): 
        dmgRoll = random.randrange(1, 21)
        if dmgRoll > 10: 
            enemy.hp -= (dmgRoll - 10) * self.damage
        elif dmgRoll < 10: 
            enemy.hp -= self.damage // (10 - dmgRoll)
        elif dmgRoll == 10:
            enemy.hp -= self.damage
