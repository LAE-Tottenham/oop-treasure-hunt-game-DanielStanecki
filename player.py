import random

class Player():
    def __init__(self, given_name):
        self.name = given_name
        self.maxHealth = 100
        self.maxEnergy = 300
        self.health = 100
        self.energy = 50
        self.inventoryMax = 30
        self.inventory = []
        self.baseDamage = 2
        self.weaponDamage = 0
        self.damage = self.baseDamage + self.weaponDamage
        self.money = 100
        
    def calculateInventory_size(self):
             return len(self.inventory) + 1

    def hurt(self, hurt): 
        self.health -= hurt
        if self.health <= 0: 
            if "Revive" in self.inventory: 
                print("You dodged death using your revive!")
                self.inventory.remove("Revive")
                self.health = self.maxHealth
            else: 
                print("Game Over!")
                exit()
        else: 
            pass

    def addItem(self, item_instance):
        if self.calculateInventory_size() < self.inventoryMax:
            self.inventory.append(item_instance.name)
        else:
            print("Your inventory is full...")

    def playerRemoveItem(self): 
        print(self.inventory)
        item = input("Please choose an item to remove: ")
        self.inventory.remove(item)

    def viewStats(self): 
        print(f"Player Health: {self.health}    Energy: {self.energy}    Damage: {self.damage}  Money: {self.money}")

    def setPlayerDMG(self, weapon): 
        self.weaponDamage = weapon.weaponDMG
        self.damage = self.baseDamage + self.weaponDamage
        
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
