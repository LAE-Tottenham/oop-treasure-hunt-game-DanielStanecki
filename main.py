from place import Place
from player import Player
from item import Item, Weapon
from enemies import Enemy
import combat

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


# weapons
sword = Weapon("Sword", 3)
hammer = Weapon("Hammer", 4)
spear = Weapon("Spear", 5)
bowAndArrow = Weapon("Bow and Arrow", 6)
greatsword = Weapon("Greatsword", 7)
axe = Weapon("Axe", 8)
mace = Weapon("Mace", 9)
magicStaff = Weapon("Magic Staff", 10)
dagger = Weapon("Dagger", 11)
goldSword = Weapon("Gold Sword", 12)
trident = Weapon("Trident", 13)
katana = Weapon("Katana", 14)
theVoidSword = Weapon("The Void Sword", 15)

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
        forgottenLake.add_next_place(crimsonsRest)
        weepingPeak.add_next_place(forgottenLake)
        weepingPeak.add_next_place(mountCrystal)
        weepingPeak.add_next_place(giantsCrossroads)
        mountCrystal.add_next_place(weepingPeak)
        mountCrystal.add_next_place(forbiddenNest)
        mountCrystal.add_next_place(theGodstree)
        giantsCrossroads.add_next_place(weepingPeak)
        giantsCrossroads.add_next_place(crimsonsRest)
        giantsCrossroads.add_next_place(forgottenPeninsula)
        crimsonsRest.add_next_place(giantsCrossroads)
        crimsonsRest.add_next_place(forgottenLake)
        forgottenPeninsula.add_next_place(giantsCrossroads)
        forgottenPeninsula.add_next_place(forbiddenNest)
        theGodstree.add_next_place(mountCrystal)
        theGodstree.add_next_place(fogCapital)
        fogCapital.add_next_place(theGodstree)
        fogCapital.add_next_place(greenLake)
        greenLake.add_next_place(fogCapital)
        greenLake.add_next_place(giantsRestingGrounds)
        giantsRestingGrounds.add_next_place(greenLake)
        giantsRestingGrounds.add_next_place(capitalOutskirts)
        capitalOutskirts.add_next_place(giantsRestingGrounds)
        capitalOutskirts.add_next_place(theCrimsonAbyss)
        theCrimsonAbyss.add_next_place(capitalOutskirts)

        #potions
        hpPotion = Item("HP Potion")
        staminaPotion = Item("Stamina Potion")


        # weapons
        sword = Weapon("Sword", 3)
        hammer = Weapon("Hammer", 4)
        spear = Weapon("Spear", 5)
        bowAndArrow = Weapon("Bow and Arrow", 6)
        greatsword = Weapon("Greatsword", 7)
        axe = Weapon("Axe", 8)
        mace = Weapon("Mace", 9)
        magicStaff = Weapon("Magic Staff", 10)
        dagger = Weapon("Dagger", 11)
        goldSword = Weapon("Gold Sword", 12)
        trident = Weapon("Trident", 13)
        katana = Weapon("Katana", 14)
        theVoidSword = Weapon("The Void Sword", 15)
        
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
        1. Go to a place
        2. Pickup item
        3. Check inventory      
        """)
        if opt == "1":
            print("You currently lack the items to go to any locations")
            pass
        elif opt == "2":
            print("""As you approach the glistening item, you start to see its shape; a long, pointed objected.
You pick it up in your hand, and you realise that it is a sword""")
            pass
        elif opt == "3":
            print(player.inventory)
            pass
        
        while opt != "2": 
            opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory      
""")
            if opt == "1":
                print("You currently lack the items to go to any locations")
                pass
            elif opt == "2":
                print("""As you approach the glistening item, you start to see its shape; a long, pointed objected.
You pick it up in your hand, and you realise that it is a sword
Your damage has increased, as you now have a weapon!""")
                sword.setPlayerDMG(player)
                pass
            elif opt == "3":
                print(player.inventory)
                pass
        
        opt = input("""In the distance, you see an cloaked figure. Would you like to approach it?
1: Yes
2: No
""")
        if opt == "1": 
            print("""As you approach, the figure turns around, and, to your terror, you see a skeleton.
The ragged skeleton reaches for its belt, and takes out a sword! 
You take out your own sword, and the fight begins!""")
            skeleton = Enemy("Skeleton ", 1, 25)
            combat.combat(player, skeleton)
game = Game()
game.setup()
game.start()
