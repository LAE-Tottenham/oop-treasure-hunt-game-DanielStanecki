class Player():
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
        

    def useItem(self, item_instance):
        if item_instance.type == "food":
            if self.energy >= self.maxEnergy - 50:
                self.energy = self.maxEnergy
            else:  
                self.energy += 50
        elif item_instance.type == "medicine":
            if self.health >= self.maxHealth - 50: 
                self.health = self.maxHealth
            else: 
                self.health += 50
       

    