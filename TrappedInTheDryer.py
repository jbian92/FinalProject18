#introduction
print("Welcome to Trapped in the Dryer! This is a text-based game where you have to find your way out of a dryer! Good luck!\n")

start = input("To begin playing, type 'play' and hit enter. Type 'help' to learn how to play. > ").lower()
while True:
    if start == "play":
        begin_game()
        break
    elif start == "help":
        help()
        break
    else:
        while start not in ("play", "help"):
            start = input("That is not a valid option. Please type 'play' or 'help'. > ")

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