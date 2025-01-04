from place import Place
from player import Player
from item import Item, Weapon, Buff
from enemies import Enemy, Boss
import time
import random

def buy(player):
    buy = input("""
    Would you like to buy a health potion? 
    1: Yes
    2: No                          
""")            
    if buy == "1": 
        if player.money >= 10: 
            player.addItem(hpPotion)
            player.money -= 10
            print("Thank you for your purchase.")
        else: 
            print("You do not have enough money to buy this.")
    else:
        print("How unfortunate, have a nice day.") 
        

def combat(player, enemy): 
    while player.health != 0 or enemy.hp != 0: 
        print("Player Turn")
        opt = input("""What would you like to do?
        1: Attack
        2: Heal
                    """)
        if opt == "1": 
            time.sleep(1.25)
            player.attack(enemy)
        elif opt == "2": 
            player.useItem(hpPotion)
        if enemy.hp <= 0: 
            print("Congratulations, you have won!")
            print(f"{enemy.name} Health: 0")
            break
        else: 
            pass
        enemy.viewStats()
        time.sleep(1.25)
        print("Enemy Turn")
        time.sleep(1.25)
        enemy.attack(player)
        if player.health <= 0: 
            print("Player Health: 0")
            print("Game Over!")
            exit()
        else: 
            player.viewStats()
        time.sleep(1.25)

def bossCombat(player, boss): 
    while player.health != 0 or boss.hp != 0: 
        print("Player Turn")
        opt = input("""What would you like to do?
        1: Attack
        2: Heal
                    """)
        if opt == "1": 
            time.sleep(1.25)
            player.attack(boss)
        elif opt == "2": 
            player.useItem(hpPotion)
        if boss.hp <= 0: 
            print("Congratulations, you have won!")
            print(f"{boss.name} Health: 0")
            break
        else: 
            pass
        boss.viewStats()
        time.sleep(1.25)
        print("Boss Turn")
        time.sleep(1.25)
        special = random.randint(1, 11)
        if special == 1:
            player.health -= boss.special
        else: 
            boss.attack(player)
        if player.health <= 0: 
            print("Player Health: 0")
            print("Game Over!")
            exit()
        else: 
            player.viewStats()
        time.sleep(1.25)

forgottenLake = Place("Forgotten Lake")
weepingPeak = Place("Weeping Peak", True)
mountCrystal = Place("Mount Crystal", True)
giantsCrossroads = Place("Giant's Crossroads", True)
crimsonsRest = Place("Crimson's Rest", True)
forgottenPeninsula = Place("Forgotten Peninsula", True)
forbiddenNest = Place("Forbidden Nest", True)
theGodstree = Place("The Godstree", True)
fogCapital = Place("Fog Capital", True)
greenLake = Place("Green Lake", True)
giantsRestingGrounds = Place("Giant's Resting Grounds", True)
capitalOutskirts = Place("Capital Outskirts", True)
theCrimsonAbyss = Place("The Crimson Abyss", True)

#potions
hpPotion = Item("HP Potion")
staminaPotion = Item("Stamina Potion")
buff = Buff("Buff")


# weapons
sword = Weapon("Sword", 3)
goldSword = Weapon("Gold Sword", 6)
hammer = Weapon("Hammer", 4)
goldHammer = Weapon("Gold Hammer", 8)
spear = Weapon("Spear", 5)
goldSpear = Weapon("Gold Spear", 10)
bowAndArrow = Weapon("Bow and Arrow", 6)
goldBowAndArrow = Weapon("Gold Bow and Arrow", 12)
greatsword = Weapon("Greatsword", 7)
goldGreatsword = Weapon("Gold Greatsword", 14)
axe = Weapon("Axe", 8)
goldAxe = Weapon("Gold Axe", 16)
mace = Weapon("Mace", 9)
goldMace = Weapon("Gold Mace", 18)
magicStaff = Weapon("Magic Staff", 10)
goldMagicStaff = Weapon("Gold Magic Staff", 20)
dagger = Weapon("Dagger", 11)
goldDagger = Weapon("Gold Dagger", 22)
nunchucks = Weapon("Nunchucks", 12)
goldNunchucks = Weapon("Gold Nunchucks", 24)
trident = Weapon("Trident", 13)
goldTrident = Weapon("Gold Trident", 26)
katana = Weapon("Katana", 14)
goldKatana = Weapon("Gold Katana", 28)
theVoidSword = Weapon("The Void Sword", 15)
theGoldVoidSword = Weapon("The Gold Void Sword", 30)

#enemies
skeleton = Enemy("Skeleton", 1, 25)
giant = Enemy("Giant", 3, 33)

#boss
fishMonster = Boss("Fish Monster", 5, 40, 10)
goatMonster = Boss("Goat Monster", 5, 42, 11)
giantWarrior = Boss("Giant Warrior", 7, 75, 13)

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        forgottenLake = Place("Forgotten Lake")
        weepingPeak = Place("Weeping Peak", True)
        mountCrystal = Place("Mount Crystal", True)
        giantsCrossroads = Place("Giant's Crossroads", True)
        crimsonsRest = Place("Crimson's Rest", True)
        forgottenPeninsula = Place("Forgotten Peninsula", True)
        forbiddenNest = Place("Forbidden Nest", True)
        theGodstree = Place("The Godstree", True)
        fogCapital = Place("Fog Capital", True)
        greenLake = Place("Green Lake", True)
        giantsRestingGrounds = Place("Giant's Resting Grounds", True)
        capitalOutskirts = Place("Capital Outskirts", True)
        theCrimsonAbyss = Place("The Crimson Abyss", True)
        
        forgottenLake.add_next_place(weepingPeak)
        weepingPeak.add_next_place(giantsCrossroads)
        mountCrystal.add_next_place(theGodstree)
        giantsCrossroads.add_next_place(crimsonsRest)
        crimsonsRest.add_next_place(forgottenPeninsula)
        forgottenPeninsula.add_next_place(forbiddenNest)
        forbiddenNest.add_next_place(mountCrystal)
        theGodstree.add_next_place(fogCapital)
        fogCapital.add_next_place(greenLake)
        greenLake.add_next_place(giantsRestingGrounds)
        giantsRestingGrounds.add_next_place(capitalOutskirts)
        capitalOutskirts.add_next_place(theCrimsonAbyss)
        theCrimsonAbyss.add_next_place(capitalOutskirts)

        self.current_place = forgottenLake
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game!")
        print("""You are a lone traveler that has found themselves in a foreign land, looking for the treasure that belongs to the Demon King Crimson. The only way to leave this fantastical world is to defeat the Demon King, and enter the void.
After entering the void, you should return back to your homeworld. However, beware. The path ahead is treacherous, and not for the faint of heart. Make sure you take your time and are strong enough during the course of the adventure""")
        name = input("Enter player name: ")
        player = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        print("You see something glistening on the ground in the distance")
        opt = input("""
        What would you like to do?
        1: Go to a place
        2: Pickup item
        3: Check inventory      
        """)
        if opt == "1":
            print("You currently lack the items to go to any locations")
            pass
        elif opt == "2":
            print("""
As you approach the glistening item, you start to see its shape; a bottle of some sorts.
You pick it up in your hand, and you realise that it is a health potion!
""")        
            player.addItem(hpPotion)
            pass
        elif opt == "3":
            print(player.inventory)
            pass
        
        while opt != "2": 
            opt = input("""
            What would you like to do?
            1: Go to a place
            2: Pickup item
            3: Check inventory      
            """)
            if opt == "1":
                print("You currently lack the items to go to any locations")
                pass
            elif opt == "2":
                print("""
As you approach the glistening item, you start to see its shape; a bottle of some sorts.
You pick it up in your hand, and you realise that it is a health potion!
""")
                player.addItem(hpPotion)
                pass
            elif opt == "3":
                print(player.inventory)
                pass
        
        opt = input("""
        In the distance, you see an cloaked figure. Would you like to approach it?
        1: Yes
        2: No
        """)
        if opt == "1": 
            print("""
As you approach, the figure turns around, and, to your terror, you see a skeleton.
The ragged skeleton reaches for its belt, and takes out a sword! 
You take out your own sword, and the fight begins!
""")
            
            combat(player, skeleton)
            dropChance = random.randint(1, 101)
            if dropChance >= 20: 
                print("The skeleton dropped a sword!")
                player.setPlayerDMG(sword)
            elif dropChance == 1: 
                print("You got a very rare weapon from the skeleton!")
                player.setPlayerDMG(goldSword)
            print("""
That is how combat works; make sure that you are strong enough to fight an enemy. 
""")
        
        print("As you walk on the shores of the lake, you see a man sitting on a bench.")
        opt = input("""
        What would you like to do? 
        1: Speak to the man
        2: Check Inventory
        3: View Stats
        """)

        if opt == "1": 
            print("""
You walk to the man, and he looks up at you.
- Hello there! Would you be interested in buy some Health Potions?
""")
            opt = input(f"""
        Would you like to buy a health potion for 15 gold. You currently have {player.money} gold.
        1: Yes
        2: No
        """)        
            if opt == "1": 
                print("- Pleasure doing business!")
                player.addItem(hpPotion)
                player.money -= 15
            
            else: 
                print("- How unfortunate. Have a pleasant day.")

        elif opt == "2": 
            print(player.inventory)
        
        elif opt == "3": 
            player.viewStats()
        
        while opt != "1": 
            opt = input("""
        What would you like to do? 
        1: Speak to the man
        2: Check Inventory
        3: View Stats
        """)
            if opt == "1": 
                print("""
You walk to the man, and he looks up at you.
- Hello there! Would you be interested in buy some Health Potions?
""")
                opt = input(f"""
        Would you like to buy a health potion for 15 gold. You currently have {player.money} gold.
        1: Yes
        2: No
        """)        
                if opt == "1": 
                    print("- Pleasure doing business!")
                    player.addItem(hpPotion)
                    player.money -= 15
            
                else: 
                    print("- How unfortunate. Have a pleasant day.")

            elif opt == "2": 
                print(player.inventory)
        
            elif opt == "3": 
                player.viewStats()
        
            

        print(f"Your health is currently {player.health}.")
        if player.health < player.maxHealth: 
            opt = input("""
        Would you like to heal? 
        1: Yes
        2: No
        """)
        
            if opt == "1": 
                player.useItem(hpPotion)
                player.viewStats()
                print(player.inventory)
        
        print("When you look into the water, you see a huge shadow swimming within")
        print("You look at it, intrigued by it, when it suddenly jumps out at you and attacks!")
        bossCombat(player, fishMonster)
        print("Congratulations, you have defeated the first boss in the game!")
        print("You find some sort of sticky gloves on the ground...")
        print("It seems that you have gotten stronger by defeating this boss...")
        buff.buffPlayer(player)


        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do now? 
    1: Try climbing the mountain using the sticky gloves. 
    2: Try swim in the lake
    3: View Inventory
    4: View Stats
    5: Heal
                    """) 
            if opt == "2": 
                print("As soon as you touch the water, you feel the poison seeping into you")
                print("You lose 10 health!")
                player.health -= 10
            elif opt == "3": 
                print(player.inventory)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                player.useItem(hpPotion)
   
        print("The gloves stick to the cliff perfectly, allowing you to easily climb it.")
        print("As you reach the top, a figure looms over you.")
        print("He speaks to you: ")
        print("- So you made it up here. Let's see if you are worthy of this adventure.")
        print("- In order for you to continue, you will have to pay me.")
        opt = input("""
    Will you pay the mysterious man? 
    1: Yes
    2: No           
""")
        if opt == "1": 
            print("- Hmph, you are a gullible one. But I'll take the money")
            player.money -= 10
        elif opt == "2": 
            print("- So you are a stubborn one. Do not worry, I was just testing your will and spirit.")

        print("As you look around, you see a great waterfall splashing into a lake.")
        print("- Welcome to the Weeping Peak")

        opt = " "
        while opt != "2":
            opt = input("""
    What would you like to do?
    1: Buy something from the merchant
    2: Drink water from the waterfall
    3: View Inventory
    4: View Stats
    5: Heal           
""")
            if opt == "1": 
                buy(player)
            elif opt == "3": 
                print(player.inventory)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                player.useItem(hpPotion)
        
        print("You take a sip of the clear water, and you feel yourself heal!")
        player.health = player.maxHealth
        player.viewStats()

        print("You walk along the small pool by the waterfall.")
        opt = input("""
    Do you want to search behind the waterfall? There is a possibilty of hidden treasure... 
    1: Yes
    2: No
    """)
        if opt == "1": 
            print("You found a treasure chest!")
            chance = random.randint(1, 101)
            if chance <= 10: 
                print("You have obtained a very rare hammer!")
                player.setPlayerDMG(goldHammer)
                print(f"Damage: {player.damage}")
            else: 
                print("You have obtained a hammer!")
                player.setPlayerDMG(hammer)
                print(f"Damage: {player.damage}")
        else: 
            pass
        found = False
        opt = " "
        while opt != "2":
            opt = input("""
    There is a cave ahead. What would you like to do? 
    1: Buy from the Merchant
    2: Enter the cave
    3: Pick up nearby item
    4: View Stats
    5: View Inventory
    6: Heal             
    """)    
            if opt == "1": 
                buy(player)
            elif opt == "3":
                if found == False:
                    print("You found a health potion and some money!")
                    player.addItem(hpPotion)
                    found = True
                else: 
                    print("There is nothing left.")
                player.money += 20
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)

        print("You enter the cave, your footsteps echoing into the darkness.")
        print("You hear footsteps coming towards you.")
        print("You see a huge goat monster walking towards you.")
        print("You take your weapon out, and prepare for battle")
        time.sleep(1.25)
        bossCombat(player, goatMonster)
        print("Congratulations, you have defeated the Goat Monster!")
        print("You see a glider laid against the cave wall. You pick it up.")
        print("It seems that defeating the boss has made you stronger....")
        buff.buffPlayer(player)
        player.health = player.maxHealth

        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do? 
    1: Glide off the mountain using your new glider
    2: Buy from the Merchant
    3: View Stats
    4: View Inventory
    5: Try climb the mountain further                    
    """)
            if opt == "2": 
                buy(player)
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                print("You try climbing the mountain, but your gloves have lost their grip!")
                print("You slip and take damage!")
                player.health -= 5

        print("You jump off the cliff, holding tightly onto the glider")
        print("After gliding for a short while, you land onto a huge crossroad")
        print("The roads are huge, and you see a huge figure sitting on the edge of the road.")
        time.sleep(2)
        print("The huge Giant walks up to you")
        print("- I have a riddle for you, in order for you to pass. ")
        ans = " "
        while ans != "candle" and ans != "a candle": 
            ans = input("""- What gets shorter the older it gets? 
            """).lower()
            if ans != "candle" and ans != "a candle": 
                print("- Incorrect, try again")
            else: 
                pass
        print("- Well done!")
        print("- You deserve a reward for this! Here is a weapon!")
        chance = random.randint(1, 101)
        if chance <= 80: 
            print("You got a spear")
            player.setPlayerDMG(spear)
        else: 
            print("You got a gold spear!! It is very rare!")
            player.setPlayerDMG(goldSpear)
        player.viewStats()
        print("- You may continue")

        print("You pass by the Giant and you come to a massive crossroad.")
        opt = " "
        found1 = False
        found2 = False
        while opt != "2": 
            opt = input("""
    Where will you go now? 
    1: Left
    2: Right
    3: Straight
    """)
            if opt == "1":
                if found1 == False: 
                    print("You take the left path and you see ")
                    print("An intimidating Giant stands there, and reaches for his spear as soon as he sees you!")
                    time.sleep(1.25)
                    combat(player, giant)
                    chance = random.randint(1, 101)
                    if chance <= 90: 
                        print("The giant dropped a spear!")
                        player.setPlayerDMG(spear)
                        player.viewStats()
                    else: 
                        print("You found a gold spear! It is very rare!")
                        player.setPlayerDMG(goldSpear)
                        player.viewStats()
                    found1 = True
                    print("There is nothing beyond, so you return back to the crossroads.")
                else: 
                    print("You have already walked this path.")
                    print("You return back to the crossroads.")
            elif opt == "3": 
                if found2 == False: 
                    print("You walk straight, and you find a treasure chest!")
                    print("Inside, you find money and a health potion.")
                    player.addItem(hpPotion)
                    player.money += 40
                    player.viewStats()
                    print("There is nothing beyond the treasure chest.")
                    print("You return to the crossroads.")
                    found2 = True
                else: 
                    print("You have already walked this path.")
                    print("You return to the crossroads.")
        
        print("You turn right, and you walk on the smooth road.")
        print("A merchant sits on a bench to the side, and there is a huge mansion ahead. ")
        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do? 
    1: Enter the mansion
    2: Buy something from the Merchant
    3: View Stats
    4: View Inventory
    5: Heal                 
    """)
            if opt == "2": 
                buy(player)
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
            
        print("You walk through the unlocked door of the mansion and wander around for a while. ")
        print("You find some money laying around. ")
        print("As soon as you touch the money, a huge Giant, wearing a complete set of chainmail armour, walks up to you, wielding a humongous hammer!")
        print("You prepare for battle!")
        bossCombat(player, giantWarrior)
        buff.buffPlayer(player)
        print("You seem to have gotten stronger...")
        player.health = player.maxHealth
        player.money += 30
        player.viewStats()
        time.sleep(1)
        print("You examine the table in the living room, and you find a map of the area!")
        print("You take the map and stuff it in your bag.")

        opt = " "
        while opt != "2": 
            opt = input("""
    What would you like to do now? 
    1: Jump off a ramp using the glider
    2: Follow the map
    3: Buy from the merchant
    4: View Stats
    5: View Inventory
    6: Heal
    """)
            if opt == "1": 
                print("You run up the ramp and jump off, but you are not high enough, and fall face flat into the mud")
                print("You take damage.")
                player.health -= 5
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)

        print("You follow the map, which leads to a place called Crimson's Rest")
        time.sleep(1.25)
        print("After a short while of walking, you reach graveyard, with red grass. ")
        print("This is Crimson's Rest")
        time.sleep(1.25)
        print("You see a larger tombstone at the centre of the cemetery and there is a man sitting on a bench to the side. ")
        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do? 
    1: Inspect the largest tombstone
    2: Speak to the man on the bench
    3: View Stats
    4: View Inventory
    5: Heal        
    """)
            if opt == "2": 
                print("You walk up to the man on the bench")
                print("He looks up at you")
                time.sleep(1.25)
                buy = input("""
    - Good day, would you be interested in buying a weapon for 40 gold?
    1: Yes
    2: No
    """)
                if buy == "1": 
                    chance = random.randint(1, 101)
                    if chance <= 95: 
                        print("You have bought a Bow and Arrow!")
                        player.setPlayerDMG(bowAndArrow)
                        player.viewStats()
                    else: 
                        print("You have bought a Gold Bow and Arrow")
                        player.setPlayerDMG(goldBowAndArrow)
                        player.viewStats()
game = Game()
game.setup()
game.start()

#test

