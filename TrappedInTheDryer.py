#This tells the player how to play the game. This will print anytime the player types in "help".
def help_info():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting with items in the game.\n")
    print(f"""These are the commands you will be using:

- 'look' or 'l': Player looks around. This repeats the description of everything you see.

- 'inventory' or 'i': This lists everything you are carrying.

- 'forward', 'left', 'right', 'back': Player walks in that direction.

- 'use ____' or 'u ____': Player uses the item. Fill in the blank with the item you want to use. You will then be asked about what you want to do with that item.
    """)
    print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")

#character setup
class Character:
    """Generic character class"""
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def stats(self):
        print(f"""{self.name}'s stats:
- health: {self.health}
- attack: {self.attack}
- defense: {self.defense}
    """)

def begin_game():
    print("hello")

#introduction to the game
print("Welcome to Trapped in the Dryer! This is a text-based game where you have to find your way out of a dryer! Good luck!\n")

start = input("To begin playing, type 'play' and hit enter. Type 'help' to learn how to play. > ").lower()
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