#This tells the player how to play the game. This will print anytime the player types in "help".
def help_info():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting with items in the game.\n")
    print(f"""These are the commands you will use the most:

- 'look' or 'l': Player looks around. This repeats the description of everything you see.

- 'examine ____' or 'x ____': Player looks more closely at something. Fill in the blank with the item you want to learn more about.

- 'inventory' or 'i': This lists everything you are carrying.

- 'forward', 'left', 'right', 'back': Player walks in that direction.

    """)
    print(f"""There are other topics you can get help on. Just type them in:

- 'help commands": This provides you with some more common commands.

- 'help hint': This provides you with a single hint on what to try next.
    """)
    print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")

#This provides the player with some more commands that can be used in the game.
def help_commands():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print(f"""These are the most common ways of interacting with the game's world. These commands do what they say. Common sense applies.

- 'take ____', 'drop ____'

- 'unlock ____ with ____', 'lock ____ with ____'

- 'open ____', 'close ____'

- 'put ____ in ____', 'put ____ on ____'

- 'touch ____', 'smell ____', 'listen to ____'

- 'eat ____', 'drink ____'

- 'search ____', 'look in ____', 'look under ____', 'look behind ____'

- 'enter ____', 'sit on ____', 'climb ____'

    """)
    print("There is no 'use' command in this game. Instead, try a command that is appropriate to whatever you are doing. If you have a book, try to 'read' it. If you find a lever, try to 'pull' or 'push' it.")
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