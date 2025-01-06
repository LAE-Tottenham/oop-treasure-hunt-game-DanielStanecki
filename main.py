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
            if "Revive" in player.inventory: 
                print("You have dodged death by using your Revive!")
                player.inventory.remove("Revive")
                player.health = player.maxHealth
            else: 
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
            if "Revive" in player.inventory: 
                print("You have dodged death by using your revive!")
                player.inventory.remove("Revive")
                player.health = player.maxHealth
            else: 
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
revive = Item("Revive")


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
ghost = Enemy("Enemy", 6, 60)
crystalDog = Enemy("Crystal Dog", 9, 80)
snake = Enemy("Snake", 11, 100)
zombie = Enemy("Zombie", 11, 110)

#boss
fishMonster = Boss("Fish Monster", 5, 40, 10)
goatMonster = Boss("Goat Monster", 5, 42, 11)
giantWarrior = Boss("Giant Warrior", 7, 75, 13)
centaur = Boss("Centaur", 8, 90, 14)
mageSpirit = Boss("Mage Spirit", 9, 100, 15)
spider = Boss("Spider", 10, 120, 17)
crystalZombie = Boss("Crystal Zombie", 14, 120, 20)
treeCreature = Boss("Tree Creature", 13, 120, 20)
assassin = Boss("Assassin", 14, 130, 21)
lostKing = Boss("The Lost King", 13, 140, 25)

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
                if player.health <= 0: 
                    print("Game Over")
                    exit()
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
                if player.health <= 0:
                    print("Game Over")
                    exit()


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
                    print("You take the left path.")
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
        player.money += 100
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
                if player.health <= 0: 
                    print("Game Over")
                    exit()
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
                choice = input("""
    - Good day, would you be interested in buying a weapon for 40 gold?
    1: Yes
    2: No
    """)
                if choice == "1": 
                    money -= 40
                    chance = random.randint(1, 101)
                    if chance <= 95: 
                        print("You have bought a Bow and Arrow!")
                        player.setPlayerDMG(bowAndArrow)
                        player.viewStats()
                    else: 
                        print("You have bought a Gold Bow and Arrow! You were very lucky to get this rare item for such a low price!")
                        player.setPlayerDMG(goldBowAndArrow)
                        player.viewStats()
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
            
        print("You approach the big tombstone, and walk around it.")
        time.sleep(1)
        print("You find a two buttons on the back of the tombstone.")
        print("Alongside the buttons, there is something written on the tombstone")
        time.sleep(1)
        opt = input("""
    - Is the number 1 a prime number? 
    1: Press the button labelled "yes"
    2: Press the button labelled "no"          
    """)
        if opt == "1": 
            print("You hear a voice shout from below!")
            print("- NO!!!!")
            time.sleep(1)
            print("A centaur leaps out from under the grave, sword and shield in hand, ready to fight you for your fatal mathematical mistake.")
            print("You prepare to fight")
            bossCombat(player, centaur)
        elif opt == "2": 
            print("You hear a voice happily shout from beneath the grave. ")
            print("A centaur leaps from under the grave, holding some sort of treasure chest in its arms")
            time.sleep(1)
            print("- Well done for solving this simple mathematical problem!")
            print("- As your reward, you can have this treasure chest! Also, you avoid my wrath, ha ha ha ha ha...")
            time.sleep(1)
            print("You open the treasure chest to find 3 health potions and lots of money!")
            player.addItem(hpPotion)
            player.addItem(hpPotion)
            player.addItem(hpPotion)
            player.money += 50
        
        print("You seem to have gotten stronger...")
        buff.buffPlayer(player)
        player.health = player.maxHealth
        print("The centaur seems to have left behind a lamp. You pick it up and put it in your bag.")
        print("You seem to have found some sort of charm that has 'Revive' written on it")
        player.addItem(revive)

        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do now?
    1: Turn the lamp on
    2: Follow the map further
    3: View Stats
    4: View Inventory
    5: Heal                  
    """)
            if opt == "2": 
                print("You follow the trail on the map, but it leads you into a trap and you take damage!")
                player.hurt(10)
                player.viewStats()
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
        
        print("You light the lamp, and you see some sort of smokey essence.")
        print("You follow the smoke, and it eventually leads you to a peninsula of some sorts.")
        time.sleep(1)
        print("You are in the Forgotten Peninsula")
        print("The area looks desolate, not a soul in sight, but you see an abandoned shack ahead")
        time.sleep(1)
        opt = " "
        found = False
        while opt != "2": 
            opt = input("""
    What would you like to do? 
    1: Pick up the nearby item
    2: Go to the abandoned shack
    3: View Stats
    4: View Inventory
    5: Heal                 
    """)
            if opt == "1": 
                if found == False: 
                    print("You walk up to the item lodged into the ground.")
                    chance = random.randint(1, 101)
                    if chance <= 85: 
                        print("You found a Greatsword!")
                        player.setPlayerDMG(greatsword)
                        player.viewStats()
                        found = True
                    else: 
                        print("You found a Gold Greatsword! It is very rare!")
                        player.setPlayerDMG(goldGreatsword)
                        player.viewStats()
                else: 
                    print("You have already picked up the item.")
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)

        print("You enter the rusty shack, and, to your surprise, a ghost attacks you!")
        time.sleep(1)
        combat(player, ghost)
        print("You have defeated the ghost!")
        print("You find a health potion on the table behind!")
        time.sleep(1)
        player.addItem(hpPotion)

        print("Also, you find the Merchant tied up, so you free him.")
        opt = " "
        while opt != "1": 
            opt = input("""
    What will you do now? 
    1: Explore the peninsula further
    2: Buy from the Merchant
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
            
        print("As you walk around the peninsula, a Mage Spirit attacks you!")
        print("You prepare for battle!")
        time.sleep(1.25)
        bossCombat(player, mageSpirit)
        print("You have defeated the Mage Spirit!")
        buff.buffPlayer(player)
        print("It seems you have gotten stronger...")
        print("In the spot where the Mage Spirit vanished, you see a medallion of some sorts on the ground.")
        time.sleep(1)
        print("You pick it up, and read 'Weaver's Medallion' on it. ")
        time.sleep(1)
        
        print("You walk forward, and come to an invisible barrier.")        
        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do now? 
    1: Insert the Weaver's Medallion into the invisble barrier
    2: Throw the lamp into the invisble barrier
    3: Buy from Merchant
    4: View Stats
    5: View Inventory
    6: Heal                  
    """)
            if opt == "2": 
                print("You hurl the lamp at the invisible barrier")
                time.sleep(1)
                print("The lamp explodes, and throws you back!")
                print("You took damage!")
                player.hurt(20)
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
        
        print("You place the medallion up against the barrier, and the invisible barrier erupts into a wall of fog!")
        time.sleep(1)
        print("You walk through the fog, to find yourself in a nest of some sorts, with webs sticking to everything.")
        print("A sign in the distance reads 'Welcome to Weaver's Nest'. ")
        time.sleep(1)
        print("You see a chest surrounded by webs, and you also see a path straight ahead. ")
        opt = " "
        found = False
        while opt != "2": 
            opt = input("""
    What would you like to do?
    1: Break the webs and open the chest
    2: Continue onwards
    3: Buy from the Merchant
    4: View Stats
    5: View Inventory
    6: Heal                   
    """)    
            if opt == "1": 
                if found == False: 
                    print("You use your hands to rip through the webs.")
                    print("You feel tired after this.")
                    player.energy -= 20
                    print("You used up some energy!")
                    player.viewStats()
                    time.sleep(1)
                    print("You open the chest and find a Health Potion and a Stamina Potion!")
                    player.addItem(hpPotion)
                    player.addItem(staminaPotion)
                    found = True
                else: 
                    print("You have already opened this chest.")
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)

        print("You walk onwards, through the hallway of webs, until you reach a huge arena.")
        time.sleep(1)
        print("You see the audience watching from all around the arena.")
        time.sleep(1)
        print("A huge spider leaps into the center of the arena, and throws you a weapon.")
        chance = random.randint(1, 101)
        if chance <= 99: 
            print("You got thrown an Axe!")
            player.setPlayerDMG(axe)
            player.viewStats()
        else: 
            print("You got thrown a Gold Axe! It is extremely rare!")
            player.setPlayerDMG(goldAxe)
            player.viewStats()
        
        time.sleep(1.25)
        print("The spider speaks")
        print("- Prepare for battle, human!")
        print("You prepare to fight!")
        time.sleep(1.25)
        bossCombat(player, spider)

        time.sleep(1.25)
        print("You have defeated the spider!")
        print("You seem to have gotten stronger...")
        buff.buffPlayer(player)
        player.health = player.maxHealth
        player.viewStats()
        print("The spider seems to have left behind some scissors, called the Silk Cutters.")
        
        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do now? 
    1: Cut through the webs and escape using the Silk Cutters.
    2: Insert the Weaver's Medallion into an opening. 
    3: Buy from the Merchant
    4: View Stats
    5: View Inventory
    6: Heal
    7: Replenish Energy                
    """)
            if opt == "2": 
                print("You insert the medallion into an opening in the door ahead.")
                print("A trapdoor opens beneath you, and you fall into it, taking damage!")
                time.sleep(1)
                print("You take damage!")
                player.hurt(15)
                time.sleep(1)
                print("You climb out of the hole.")
            elif opt == "3": 
                buy(player)
            elif opt ==  "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
            elif opt == "7": 
                player.useItem(staminaPotion)

        print("You use the silk cutters to tear through the webs covering the door way. ")
        time.sleep(1)
        print("You open the door, and walk through it.")
        time.sleep(1)
        print("You find yourself on another mountain, and you see a huge crystal on the peak of the mountain.")
        time.sleep(1)
        print("You see some sort of building below the crystal, and a dog of some sorts resting on the side.")
        opt = " "
        while opt != "2": 
            opt = input("""
    What would you like to do
    1: Go to the dog
    2: Go to the building
    3: View Stats
    4: View Inventory
    5: Heal
    6: Replenish Energy       
    """)    
            if opt == "1": 
                print("You walk up to the dog, and you realise it has crystals growing on its back!")
                time.sleep(1)
                print("The dog turns around and bares its teeth at you!")
                print("You take your sword out!")
                time.sleep(1)
                combat(player, crystalDog)
                chance = random.randint(1, 101)
                if chance <= 95: 
                    print("You got a mace!")
                    player.setPlayerDMG(mace)
                    player.viewStats()
                else: 
                    print("You got a gold mace! It is very rare!")
                    player.setPlayerDMG(goldMace)
                    player.viewStats()
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
            elif opt == "6": 
                player.useItem(staminaPotion)
        
        print("You go towards the building but it seems to be locked")
        opt = ("""
    What do you do? 
    1: Break it down
    2: Knock on it politely           
    """)
        if opt == "1": 
            print("You barge into the building, and you find a crystal creature resting inside")
            print("- Who are you! Why are you here!")
            time.sleep(1)
            print("The creature takes its weapon out, and prepares to fight!")
            print("You prepare for battle!")
            time.sleep(1)
            bossCombat(player, crystalZombie)
            print("You have defeated the crystal zombie!")
            print("You find a Golden Key laying on the table, and take it.")
            print("Are you happy now that you have disrupted an innocents creature its life? ")
            player.morality -= 1
        else: 
            print("You hear footsteps heading towards the door.")
            time.sleep(1.25)
            print("When the door opens, you see a humanoid crystal.")
            print("- Why, hello there!, Welcome, adventurer, I've been awaiting you!")
            time.sleep(1)
            print("- I have something that may be useful for your journey.")
            print("The crystal creature gives you a health potion and some money.")
            print("Also, he gives you a Golden Key.")
            player.addItem(hpPotion)
            player.money += 40
            player.morality += 1
        
        print("You exit the house.")
        print("You seem to have gotten stronger...")
        buff.buffPlayer(player)
        opt = " "
        while opt != "1": 
            opt = ("""
    What would you like to do now? 
    1: Use the Golden Key to open the huge door into the mountain
    2: Try to cut through the crystal using the Silk Cutters
    3: Buy from the Merchant
    4: View Stats
    5: View Inventory
    6: Heal
    7: Replenish Energy               
    """)
            if opt == "2": 
                print("You try to cut the crystal, but just end up cutting yourself!")
                print("You take damage!")
                player.hurt(10)
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
            elif opt == "7": 
                player.useItem(staminaPotion)

        print("You walk up to the huge door in the mountain and insert the Golden Key into the small keyhole.")
        time.sleep(1)
        print("You push the door open and enter slowly.")
        print("You walk through the corridor in the mountain, and soon emerge on the other side.")
        print("You see a huge, golden tree, and nearby, a sign saying 'The Godstree'. ")
        time.sleep(1)
        print("On your left, you see a chest, while straight ahead is a ladder to the top of the tree")
        opt = " "
        found = False
        while opt != "2": 
            opt = input("""
    What will you do? 
    1: Open the chest
    2: Climb the ladder ahead
    3: View Stats
    4: View Inventory
    5: Heal
    6: Replenish Energy                    
    """)
            if opt == "1": 
                print("You go to the chest and try to open it.")
                print("It requires a lot of energy.")
                if player.energy < 100: 
                    print("You were unable to open the chest, as you lack the energy for it.")
                else: 
                    print("You opened the chest and found a weapon!")
                    chance = random.randint(1, 101)
                    if chance <= 90: 
                        print("You got a Magic Staff!")
                        player.setPlayerDMG(magicStaff)
                        player.viewStats()
                    else: 
                        print("You got a Gold Magic Staff! It is very rare!")
                        player.setPlayerDMG(goldMagicStaff)
                        player.viewStats()
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
            elif opt == "6": 
                player.useItem(staminaPotion)
        
        print("You climb the gold ladder, and reach the top.")
        time.sleep(1)
        print("You see a throne of some sorts, but it seems unoccupied.")
        print("There is also a statue")
        opt = input("""
    What will you do? 
    1: Rest and sit on the throne
    2: Give an offering to the statue           
    """)    
        if opt == "1": 
            print("You sit on the throne, and rest for a while.")
            time.sleep(2)
            print("z")
            time.sleep(2)
            print("Z")
            time.sleep(2)
            print("z")
            print("You wake up, and see a tree creature standing in front of you, with a staff in hand.")
            print("- You are in my seat, human, and for that, you will pay!")
            time.sleep(1)
            print("You prepare for battle!")
            bossCombat(player, treeCreature)
            print("You have defeated the tree creature.")
            print("You see mask laying on the ground, so you take it.")
            player.morality -= 1
        else: 
            print("You leave a few coins at the base of the statue.")
            player.money -= 20
            time.sleep(1)
            print("You hear a humming sound, and suddenly, you have 100 coins in your pocket!")
            player.money += 100
            print("You also find a health potion")
            player.addItem(hpPotion)
            print("A mask also lays by the statue, so you take it.")
            player.morality += 1
        
        print("You inspect the mask, and it seems to show hidden routes when looked through.")
        time.sleep(1)
        print("You feel yourself getting stronger...")
        buff.buffPlayer(player)
        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do? 
    1: Follow the hidden route shown in the Clarifying Mask
    2: Try inserting the key into the statue
    3: Buy from the Merchant
    4: View Stats
    5: View Inventory
    6: Heal
    7: Replenish Energy                    
    """)
            if opt == "2": 
                print("You insert the key into the hole in the statue.")
                print("The ground rumbles, and a spike ejects from the statue, grazing your skin!")
                time.sleep(1)
                print("You took damage")
                player.hurt(15)
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
            elif opt == "7": 
                player.useItem(staminaPotion)

        print("You follow the hidden route, which eventually leads to a foggy city.")
        print("You are now in Fog Capital, a city stuck between reality and the dream state. ")
        time.sleep(1)
        print("There are stairs leading down.")
        opt = " "
        while opt != "2": 
            opt = input("""
    What will you do? 
    1: Take off the Clarifying Mask
    2: Follow the stairs downwards
    3: View Stats
    4: View Inventory
    5: Heal
    6: Replenish Energy                     
    """)
            if opt == "1": 
                print("You take the mask off, and realise you are in an empty desert.")
                time.sleep(1)
                print("How you got here, you have no idea, but what you do know is that there is a snake coming towards you really fast!")
                time.sleep(1)
                print("You prepare to fight!")
                combat(player, snake)
                print("You have defeated the snake!")
                chance = random.randint(1, 101)
                if chance <= 97: 
                    print("You got a dagger!")
                    player.setPlayerDMG(dagger)
                    player.viewStats()
                else: 
                    print("You got a Gold Dagger! It is very rare!")
                    player.setPlayerDMG(goldDagger)
                    player.viewStats()
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5":
                player.useItem(hpPotion)
            elif opt == "6": 
                player.useItem(staminaPotion)

        print("You walk down the foggy stairs, and you find yourself in a chamber.")
        time.sleep(1)
        print("You have a choice to make; either go left or go right.")
        opt = input("""
    Where will you go? 
    1: Left
    2: Right                
    """)
        if opt == "1": 
            print("You go left, leading you into a maze.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("...You finally make it out of the maze only to realise you are back in the chamber")
        else: 
            pass
                       
        print("You go right, and you find yourself in an extremely foggy room.")
        print("You hear very quiet footsteps, and suddenly a cloaked figure jumps at you!")
        time.sleep(1)
        print("You prepare for battle!")
        bossCombat(player, assassin)
        print("You have beaten the enemy!")
        time.sleep(1)
        print("The mask has been knocked off your face, and you realise that you are in some forest.")
        print("Also, you find a vial on the ground, labelled 'Poison Immunity'. ")
        
        print("You seem to have gotten stronger...")
        buff.buffPlayer(player)
        print("You find money laying around on the dirt.")
        player.money += 30

        print("As you walk, you start to feel yourself choke. ")
        opt = " "
        while opt != "1": 
            opt = input("""
    What will you do? 
    1: Drink the Poison Immunity
    2: Put the Clarifying Mask back on
    3: Buy from the Merchant
    4: View Stats
    5: View Inventory
    6: Heal
    7: Replenish Energy                    
    """)
            if opt == "2": 
                print("You put the mask on, but you are still choking!")
                player.hurt(20)
                player.viewStats()
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
            elif opt == "7": 
                player.useItem(staminaPotion)

        print("You drink the vial, and you feel a sensation coming over you.")
        time.sleep(1)
        print("You stop choking. It seems that there was some poisonous substance in the air. ")
        time.sleep(1)
        print("You walk through the clearing, and come out onto a clearing, with a mossy lake in the middle.")
        print("A sign nearby reads 'Green Lake'. ")
        time.sleep(1)
        print("In the distance, you see a small shack. ")

        found = False
        opt = " "
        while opt != "1": 
            opt = input("""
    What will you do? 
    1: Swim in the water
    2: Search the shack
    3: View Stats
    4: View Inventory
    5: Heal
    6: Replenish Energy                   
    """)        
            if opt == "2":
                if found == False: 
                    print("You enter the shack, and inside is a small box.")
                    print("You open the box, to find a lot of money!")
                    print("Also, there is a revival charm inside!")
                    chance = random.randint(1, 101)
                    if chance <= 95: 
                        print("You also find nunchucks on the side!")
                        player.setPlayerDMG(nunchucks)
                        player.viewStats()
                    else: 
                        print("You also find Gold Nunchucks on the side! They are very rare!")
                        player.setPlayerDMG(goldNunchucks)
                        player.viewStats()
                    player.addItem(revive)
                    player.money += 50
                    found = True
                else: 
                    print("You have already found everything in this shack.")
            elif opt == "3": 
                player.viewStats()
            elif opt == "4": 
                print(player.inventory)
            elif opt == "5": 
                player.useItem(hpPotion)
            elif opt == "6": 
                player.useItem(staminaPotion)

        print("You dive into the water, and sense your poison immunity protecting you from the poison in the water. ")
        time.sleep(1)
        print("You swim for a while, until you reach the shore at the other end of the lake. ")
        print("A large statue of a king is placed here.")
        time.sleep(1)
        print("You see some gold coins on the ground by the statue.")
        
        opt = input("""
    What will you do? 
    1: Take the coins 
    2: Leave the coins
    """)    
        if opt == "1": 
            print("You snatch the coins from the statue, and walk away. You think you heard a groaning sound but you ignore it.")
            player.money += 30
            time.sleep(2)
            print("BOOM!")
            print("The statue explodes, and out of it leaps out a large figure, shaped just like the statue!")
            time.sleep(1)
            print("- You dare steal money from the king!")
            print("You prepare to fight!")
            bossCombat(player, lostKing)
            print("You have defeated the Lost King!")
            player.morality -= 1
        else: 
            print("You leave the money by the statue and continue on your way")
            player.morality += 1

        print("Behind the statue, you find a shovel.")
        print("You seem to have gotten stronger...")
        buff.buffPlayer(player)
        time.sleep(1)
        print("You see an odd patch of dirt ahead.")

        opt = " "
        while opt != "1": 
            opt = input("""
    What would you like to do? 
    1: Dig through the suspicious dirt
    2: Swim back through the lake
    3: Buy from the merchant
    4: View Stats
    5: View Inventory
    6: Heal
    7: Replenish Energy                   
    """)
            if opt == "2": 
                print("You enter the water, but it seems your poison immunity has worn off!")
                time.sleep(1)
                print("You rush out of the water!")
                player.hurt(10)
            elif opt == "3": 
                buy(player)
            elif opt == "4": 
                player.viewStats()
            elif opt == "5": 
                print(player.inventory)
            elif opt == "6": 
                player.useItem(hpPotion)
            elif opt == "7": 
                player.useItem(staminaPotion)

        print("You start digging the dirt...")
        time.sleep(2)
        print("You finish digging, and you find a staircase!")
        print("You go down the stairs.")
        time.sleep(2)
        print("You get to the base of the stairs, and you see a huge tomb.")
        print("You are in the Giant's Resting Grounds")
        print("There are bones on the ground, and webs everywhere.")
        print("Also, there is a corridor into another room.")
        
        found = False
        opt = " "
        while opt != "2": 
            opt = ("""
    What would you like to do? 
    1: Explore the other corridor
    2: Examine the Giant's tombstone
    3: View Stats
    4: View Inventory
    5: Heal
    6: Replenish Energy               
    """)
            if opt == "1": 
                if found == False: 
                    print("You enter the corridor, and see a smaller tomb.")
                    time.sleep(1)
                    print("You inspect the tomb, when suddenlt, a zombie jumps out, wielding a trident!")
                    print("You prepare for battle!")
                    time.sleep(1)
                    combat(player, zombie)
                    print("You have defeated the zombie!")
                    time.sleep(1)
                    print("There is a weapon laying on the side of the tomb.")
                    chance = random.randint(1, 101)
                    chance 

game = Game() 
game.setup()
game.start()

#test


