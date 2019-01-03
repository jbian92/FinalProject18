#This tells the player how to play the game.
def help_info():
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("You will be exploring places and interacting with items in the game.\n")
    print("You will be asked a question as to what you would like to do. You will be given the choices within the question.\n")
    print(f"""For example:
Do you want to 'go through the door' or 'walk up the stairs'?
You can either type in 'go through the door' or 'walk up the stairs'. The commands you can use will be in quotes.""")
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

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