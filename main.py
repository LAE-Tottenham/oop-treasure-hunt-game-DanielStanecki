from place import Place
from player import Player
from item import Item, Weapon

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
        forgottenLake.add_next_place(greenLake)
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

        # etc. 
        
        # items
        hammer = Item('Hammer')
        pen = Item('Pen')

        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = forgottenLake
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        name = input("Enter player name: ")
        player = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
etc.      
""")
        if opt == "1":
            # add code
            pass
        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass
            
