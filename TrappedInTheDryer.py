import sys

#This is for the player to press enter to continue with the descriptions in the game. This will break up the description so it would be easier to read.
def x():
    x = input("")
    return x

#This is for when the player types in an invalid command.
def invalid():
    print("Sorry but the command you entered is invalid. Please type in a command that is shown in quotes.")
    return

#Before beginning the game, the player can choose to either begin or learn how to play.
def start():
    start = input("To begin playing, type 'play' and press enter. Type 'help' to learn how to play. > ").lower()
    while True:
        if start == "play":
            begin_game()
            break
        elif start == "help":
            help_info()
            break
        else:
            while start not in ("play", "help"):
                start = input("That is not a valid option. Please type 'play' or 'help'. > ")
    return

#This tells the player how to play the game.
def help_info():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting with items in the game. After every line of text that does not require a command, press enter to continue.")
    x()
    print("You will be asked a question as to what you would like to do. You will be given the choices within the question.")
    x()
    print(f"""For example:
Do you want to 'go through the door' or 'walk up the stairs'?
You can either type in 'go through the door' or 'walk up the stairs'. The commands you can use will be in quotes.""")
    x()
    print("You will need to type in a command if you see '>' after a line of text.")
    x()
    print("If you are not given a command to use and you do not see '>' at the end of the text, you are most likely being given a description. You will need to press enter to continue.\n")
    print("~ Press enter to continue. ~")
    x()
    print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    start()
    return

#character setup
class Character:
    """Generic character class"""

    #displays health, attack, and defense of character
    def stats(self):
        print(f"""{self.name}'s stats:
- health: {self.health}
- attack: {self.attack}
- defense: {self.defense}
    """)

#player's character setup
class Player(Character):
    """Generic player class"""

    def __init__(self):
        """Constructor for Player class"""
        self.name = input("\nWhat is your name? > ")

        self.health = 100
        self.attack = 5
        self.defense = 20

        self.inventory = {
            "weapons": {
                "sock": 1,
                "hairpin": 0,
                "hair comb": 0,
            },
            "food": {
                "gum": 0,
                "hard candy": 0
            }
        }

    #shows the player's inventory
    def invt(self):
        for k, v in self.inventory.items():
            print(f"{k}:")
            for k_, v_ in self.inventory[k].items():
                print(f" - {k_} ({v_})")

    def battle(self, opponent):
        """Player fights opponent"""
        print("Let the battle begin!")
        x()
        while player.health > 0 and opponent.health > 0:
            print(f"You attack {opponent.name}.")
            x()
            dmg_player = self.attack - opponent.defense
            if dmg_player <= 0:
              dmg_player = 0
            opponent.health -= dmg_player
            print(f"{opponent.name} is down to {opponent.health} health.")
            x()
            if player.health > 0 and opponent.health > 0:
                print(f"{opponent.name} attacks you.")
                x()
                dmg_opponent = opponent.attack - player.defense
                if dmg_opponent <= 0:
                  dmg_opponent = 0
                player.health -= dmg_opponent
                print(f"You are down to {player.health} health.")
                x()
            else:
                break
        if player.health > 0 and opponent.health <= 0:
            print("You won the battle! Congratulations!")
        else:
            print("Sorry, you lost.")
        return

#opponent character setup
class Opponent(Character):
    """Generic opponent class"""

    def __init__(self, name, health, attack, defense):
        """Constructor for Opponent class"""
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

#These are the opponents in the game.
rat = Opponent("The Rat", 15, 25, 5)

#These are the items that need to be unlocked by the player during the game.
open_lever = "locked"
open_metal_door = "locked"

#Heating Duct Room
def heating_duct():

    print("\nYou get on your knees and crawl through the small gap.")
    x()
    print("~ checkpoint ~")
    x()

    #This is the description of the room.
    print("You are now standing in the Heating Duct Room. The room is warm and cozy. In 'front' of you, you see a door slightly open. However, you cannot see beyond the door. Behind you, there is a 'gap' in the wall.\n")

###HOW TO NOT FIGHT THE RAT AGAIN IF COME BACK TO THIS ROOM AFTER WIN THE BATTLE
    rat_battle = "no"

    c2 = input("> ").lower()
    while True:
        if c2 == "front":
            while True:
                if rat_battle == "no":
                    print("\nYou open the door and walk inside. You hope that the heating duct will lead you out of the dryer, but once your eyes finished adjusting to the darkness, you see a rat right in front of you.")
                    x()
                    print("The rat is remarkably large and well-fed. It seems to be angry at you. You may get into a fight with a rat today. *sigh*")
                    x()
                    player.stats()
                    x()
                    rat.stats()
                    x()
                    print("You have a weapon in your inventory!")
                    x()
                    player.invt()
                    x()
                    print("You can use your sock that you were trying to grab as a weapon against the rat.")
                    player.attack += 5
                    x()
                    print(f"The sock increases your attack to {player.attack}.")
                    x()
                    player.battle(rat)
                    x()
                    #There is no code for if the player loses the battle because the game is designed for the player to win this battle.
                    rat_battle = "yes" #########???
                    print("Behind the fallen rat, you see a hairpin.")
                    x()
                    player.inventory['weapons']['hairpin'] += 1
                    print("~ New weapon acquired: hairpin ~")
                    x()
                    print("You continue walking past the rat, but it becomes too steep for you to continue walking. You cannot get out of the dryer this way. You turn around and return to the Heating Duct Room.")
                    x()
                    print("You are now standing in the Heating Duct Room. The room is warm and cozy. In 'front' of you, you see a door slightly open, which is where you just came from. Behind you, there is a 'gap' in the wall.\n")
                    c2 = input("> ").lower()
                    break

                else:
                    print("\nYou open the door and walk inside. You hope that the heating duct will lead you out of the dryer, but once your eyes finished adjusting to the darkness, you see a dead rat in front of you. You remember that this was where you fought with the rat. You turn around and go back.")
                    x()
                    print("You are now standing in the Heating Duct Room. The room is warm and cozy. In 'front' of you, you see a door slightly open, which is where you just came from. Behind you, there is a 'gap' in the wall.\n")
                    c2 = input("> ").lower()
                    break

        elif c2 == "gap":
            print("\nYou get on your knees and crawl through the small gap.\n")
            drum_room()
            break

        else:
            while c2 not in ("front", "gap"):
                invalid()
                c2 = input("> ").lower()
                break

    return

#               game = input("You were not able to complete the game. Do you want to go back to your last 'checkpoint' or 'stop' playing? > ").lower()
                #if game == "checkpoint":
                #    heating_duct()
                #else:
                #    sys.exit()

#Dryer Drum Room - This is the room where the player starts in.
def drum_room():

    #This is the description of the room.
    print("You are now in the Dryer Drum Room. The room is dark and cold. It seems to be in the shape of a cylinder. Right behind you is the 'dryer door'. Next to the dryer door, there is a ‘lever’ inside a glass box. In 'front' of you, there is a gap in the wall. To the 'left', there is metal door. To the 'right', stairs ascend into darkness.\n")

    c1 = input("> ").lower()
    while True:
        if c1 == "dryer door":
            print("The dryer door is closed and locked. It seems to be connected to the lever.")
            c1 = input("> ").lower()
            break

        elif c1 == "lever":
            if open_lever == "locked":
                print("The box is closed and locked. You cannot get to the lever. However, there is a keyhole.")
                c1 = input("> ").lower()
                break

            #This is the end of the game.
            else:
                print()

                break

        elif c1 == "front":
            heating_duct()
            break

        elif c1 == "left":
            if open_metal_door == "locked":
                print("The door is closed and locked.")
                c1 = input("> ").lower()
                break
            else:
                print()

                break

        elif c1 == "right":
            blower_room()
            break

        else:
            while c1 not in ("dryer door", "lever", "front", "left", "right"):
                invalid()
                c1 = input("> ").lower()
                break

    return

#This is the game the player will be playing.
def begin_game():

    #background information
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("It's laundry day! Yay!... yeah no. You are at the laundromat with your bundle of clothes. Thankfully, you only have to wait for your clothes to finish drying in the dryer before you can finally go home.")
    x()
    print(".")
    x()
    print(".")
    x()
    print(".")
    x()
    print("And the dryer finally stopped! You begin taking out your clothes, excited to go back home and binge watch Netflix on the couch.")
    x()
    print("Wait, wait, wait. Before you close the dryer door, you realize that there's a sock stuck at the very back of the dryer. You reach for the sock but your arm seems to be too short to reach the back. You decide to crawl into the dryer to get your sock back.")
    x()
    print("Your body is halfway inside the dryer but the sock still seems so far away. You keep crawling until your body is completely inside the dryer. You look around, amazed at how big the dryer is.")
    x()
    print("You can finally reach the sock. However, as soon as your fingers touch the sock, the dryer turns back on and you feel yourself slowly turning along with the dryer drum. The spinning starts to get faster but you can't seem to get out!")
    x()
    print(".")
    x()
    print(".")
    x()
    print(".")
    x()
    print("After what seems like forever, the spinning finally stops. You slowly get up, a bit dizzy from all that spinning. You look around and realize that you have shrunk and are now stuck inside the dryer.")
    x()
    print("~ Remember that anything in quotes ' ' can be used as a command. ~")
    x()

    drum_room()

#introduction to the game
print("Welcome to Trapped in the Dryer! This is a text-based game where you have to find your way out of a dryer! Good luck!")
player = Player()
print("\n")
start()