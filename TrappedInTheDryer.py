###################################
# NEEDED FOR THE GAME TO FUNCTION #
###################################
import sys
import random

#############################################
# FUNCTIONS THAT ARE USED OFTEN IN THE GAME #
#############################################

#This is for the player to press enter to continue with the descriptions in the game. This will break up the description so it would be easier to read.
def x():
    x = input("")
    return x

#This is for when the player types in an invalid command.
def invalid():
    print("\nSorry but the command you entered is invalid. Please type in a command that is shown in quotes.")
    return

################################
# INFO BEFORE PLAYING THE GAME #
################################

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

######################
# CHARACTERS IN GAME #
######################

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
            },
            "clothes": {
            },
            "food": {
            },
            "items": {
            }
        }

    #shows the player's inventory
    def invt(self):
        for k, v in self.inventory.items():
            print(f"{k}:")
            for k_, v_ in self.inventory[k].items():
                print(f" - {k_} ({v_})")
            print(" ")
        return

    def battle(self, opponent):
        """Player fights opponent"""
        print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")
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
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print(" ~ YOU DIED! ~")
            x()
            print("              ______               ")
            print("        _____/      \\_____        ")
            print("       |  _     ___   _   ||       ")
            print("       | | \     |   | \  ||       ")
            print("       | |  |    |   |  | ||       ")
            print("       | |_/     |   |_/  ||       ")
            print("       | | \     |   |    ||       ")
            print("       | |  \    |   |    ||       ")
            print("       | |   \. _|_. | .  ||       ")
            print("       |                  ||       ")
            print("       |                  ||       ")
            print("       |                  ||       ")
            print("       | *   **    * **   |**      ")
            print("  \))/.,(//,,..,,\||(,,.,\\,.((//  ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        return

    def battle_boss(self, opponent):
        """Player fights final boss"""
        print("- - - - - - - - - - - - - - - - - - - - - - - - -\n")
        print("Let the battle begin!")
        x()
        while player.health > 0 and opponent.health > 0:
            f1 = input("Do you want to 'attack' or 'defend'? > ").lower()
            while True:
                if f1 == "attack":
                    print(f"\nYou attack {opponent.name}.")
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
                        break
                    else:
                        break
                elif f1 == "defend":
                    print(f"\n{opponent.name} attacks you.")
                    x()
                    print("You take no damage.")
                    x()
                    break
                else:
                    while f1 not in ('attack', 'defend'):
                        print("")
                        invalid()
                        f1 = input("Do you want to 'attack' or 'defend'? > ").lower()
        if player.health > 0 and opponent.health <= 0:
            print("You won the battle! Congratulations!")
            solved['open_lever'] = True
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print(" ~ YOU DIED! ~")
            x()
            print("              ______               ")
            print("        _____/      \\_____        ")
            print("       |  _     ___   _   ||       ")
            print("       | | \     |   | \  ||       ")
            print("       | |  |    |   |  | ||       ")
            print("       | |_/     |   |_/  ||       ")
            print("       | | \     |   |    ||       ")
            print("       | |  \    |   |    ||       ")
            print("       | |   \. _|_. | .  ||       ")
            print("       |                  ||       ")
            print("       |                  ||       ")
            print("       |                  ||       ")
            print("       | *   **    * **   |**      ")
            print("  \))/.,(//,,..,,\||(,,.,\\,.((//  ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
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
lint = Opponent("The Lint Monster", 80, 30, 8)
ghost = Opponent("Steve the Ghost", 20, 25, 3)
final_boss = Opponent("The Discarded Laundry Monster", 100, 30, 5)

########
# GAME #
########

#These are the things that need to be unlocked/solved by the player during the game.
solved = {'heating_duct': False, 'open_lever': False, 'open_metal_door': False, 'lint_room': False, 'motor_room': False, 'mask': False, 'hairpin': False, 'motor': False, 'candy': False}

#This is the game the player will play in the Motor Room - guess the number Steve the Ghost is thinking of.
def guessing_game():
    secret = random.randint(0,20)
    num_guesses = 0
    guesses_left = 10

    while num_guesses < 10:
      guess = int(input("\nSteve: Pick a number between 0 and 20. > "))
      num_guesses = num_guesses + 1
      guesses_left = guesses_left - 1
      if guess > secret:
        print(f"\nSteve: Your guess is too high. You have {guesses_left} guesses left.")
      elif guess < secret:
        print(f"\nSteve: Your guess is too low. You have {guesses_left} guesses left.")
      else:
        break

    if guess == secret:
        solved['motor_room'] = True

    return

#Heating Duct Room - Player will fight a rat to obtain a new weapon that will help defeat future opponents.
def heating_duct():

    print("\nYou get on your knees and crawl through the small gap.")
    x()
    print("~ checkpoint ~")
    x()

    #This is the description of the room.
    print("You are now standing in the Heating Duct Room. The room is warm and cozy. In 'front' of you, you see a door slightly open. However, you cannot see beyond the door. Behind you, there is a 'gap' in the wall.\n")

    c2 = input("> ").lower()
    while True:
        if c2 == "front":
            while True:

                #if the player did not complete the Heating Duct Room
                if solved['heating_duct'] == False:
                    print("\nYou open the door and walk inside. You hope that the heating duct will lead you out of the dryer, but once your eyes finished adjusting to the darkness, you see a rat right in front of you.")
                    x()
                    print('          __             _,-"~^"-.                                ')
                    print('        _// )      _,-"~`         `.                              ')
                    print('      ." ( /`"-,-"`                 ;                             ')
                    print('     / 6                             ;                            ')
                    print('    /           ,             ,-"     ;                           ')
                    print('   (,__.--.      \           /        ;                           ')
                    print("    //'   /`-.\   |          |        `._________                 ")
                    print("      _.-'_/`  )  )--...,,,___\     \-----------,)                ")
                    print("""    ((("~` _.-'.-'           __`-.   )         //                """)
                    print('          ((("`             (((---~"`         //                  ')
                    print('                                             ((________________   ')
                    print('                                             `----""""~~~~^^^```  ')
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
                    solved['heating_duct'] = True
                    print("Behind the fallen rat, you see a hairpin.")
                    x()
                    player.inventory['weapons']['hairpin'] = 1
                    solved['hairpin'] = True
                    print("~ New weapon acquired: hairpin ~")
                    x()
                    player.attack += 10
                    print(f"The hairpin increases your attack to {player.attack}.")
                    x()
                    print("You continue walking past the rat, but it becomes too steep for you to continue walking. You cannot get out of the dryer this way. You turn around and return to the Heating Duct Room.")
                    x()
                    print("You are now standing in the Heating Duct Room. The room is warm and cozy. In 'front' of you, you see a door slightly open, which is where you just came from. Behind you, there is a 'gap' in the wall.\n")
                    c2 = input("> ").lower()
                    break

                #if the player has completed this room
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

    return

#Air Flow Room -
def air_flow():

    #This is the description of the room.
    print("You are now standing in the Air Flow Room. On the floor, you see a 'face mask'. To the 'right', there is an open metal door.")

    c5 = input("> ").lower()
    while True:
        if c5 == "face mask":
            player.inventory['clothes']['face mask'] = 1
            solved['mask'] = True
            print("\n~ New clothes acquired: face mask ~")
            x()
            print("The face mask looks like the one surgeons and doctors wear. It should be useful if you want to lessen your air pollution exposure.\n")
            c5 = input("> ").lower()
        elif c5 == "right":
            print("")
            drum_room()
            break
        else:
            while c5 not in ('face mask', 'right'):
                invalid()
                c5 = input("> ").lower()

    return

#Heating Element Room -
def heating_element():

    #This is the description of the room.
    print("\nYou are now standing in the Heating Element Room.")

    if solved['open_lever'] == False:
        print("\n???: I heard that you want to get out of this dryer. I am The Discarded Laundry Monster! You must defeat me to escape!")
        x()
        player.stats()
        x()
        final_boss.stats()
        x()
        player.battle_boss(final_boss)

    else:
        print("You have beaten the final boss. You should try and get out of the dryer.")

        #continuation of description
        print("")

    return

#Belt Tensioner Room -
def belt_tensioner():

    #This is the description of the room.
    print("")

#Lint Trap Room -
def lint_trap():

    #This is the description of the room.
    print("You are now standing in the Lint Trap Room. The room is very dusty, and you immediately start coughing.")
    x()

    #if the player has not completed the Lint Trap Room
    if solved['lint_room'] == False:
        print("*COUGH! COUGH! COUGH!")
        x()
        print("Oh no! It looks like you aren't alone in the room. Your coughing probably disturbed its sleep. The creature looked as if it was made out of lint...")
        x()
        print("*COUGH! COUGH! COUGH!")
        x()

        #The player can attack The Lint Monster only if they found the face mask in the Air Flow Room.
        if solved['mask'] == True:
            print("You remember that you have a face mask in your inventory. You quickly put it on to stop coughing.")
            x()
            print("You look up and catch the creature trying to sneak up at you. You both freeze.")
            x()
            player.stats()
            x()
            lint.stats()
            x()
            print("It seems like you'll have to fight the creature. ugh -_- . You just wanted to go home and watch Netflix, but no, here you are.")
            x()

            #The player can complete this room only if they got the hairpin after fighting The Rat.
            if solved['hairpin'] == True:
                print("On the bright side, you can use your new weapon, hairpin, to stab The Lint Monster!")
                x()
                player.invt()
                x()
                player.battle(lint)
                x()
                #The game is programmed for the player to win the battle if they have the hairpin.
                solved['lint_room'] = True

                #continuation of description
                print("The room is still dusty. In the corner of the room, you see a locked 'box' covered in spider webs and dust. To the 'right', there is a small flap covering a hole. 'Behind' you and to the 'left' are two archways.\n")

                #if the player completed the Motor Room
                if solved['motor_room'] == True:
                    c4 = input("> ").lower()
                    while True:
                        if c4 == "box":
                            if solved['candy'] == False:
                                print("\nYou remember that the ghost from the Motor Room unlocked something for you. You think it may be this box.")
                                x()
                                print("The box opened! Inside, you find candy?")
                                x()
                                player.inventory['food']['candy'] = 1
                                print("~ New food acquired: candy ~")
                                solved['candy'] = True
                                x()
                                player.health += 100
                                print(f"The candy increases your health to {player.health}.")
                                x()
                            else:
                                print("The box is empty.")
                            c4 = input("> ").lower()
                        elif c4 == "right":
                            print("\nYou get on your knees before pulling the flap up and crawling inside.")
                            x()
                            blower_room()
                            break
                        elif c4 == "behind":
                            heating_element()
                            break
                        elif c4 == "left":
                            belt_tensioner()
                            break
                        else:
                            while c4 not in ('box', 'right', 'behind', 'left'):
                                invalid()
                                c4 = input("> ").lower()

                #if the player did not complete the Motor Room
                else:
                    c4 = input("> ").lower()
                    while True:
                        if c4 == "box":
                            print("The box is locked, but you don't see a keyhole. You may need someone's help to open it.\n")
                            c4 = input("> ").lower()
                        elif c4 == "right":
                            print("\nYou get on your knees before pulling the flap up and crawling inside.")
                            blower_room()
                            break
                        elif c4 == "behind":
                            heating_element()
                            break
                        elif c4 == "left":
                            belt_tensioner()
                            break
                        else:
                            while c4 not in ('box', 'right', 'behind', 'left'):
                                invalid()
                                c4 = input("> ").lower()

            #The player will fail if they fight with the sock.
            else:
                print("You decide to continue fighting with your trusty sock.")
                x()
                player.battle(lint)
                x()
                game = input("You were not able to complete the game. Do you want to go back to your last 'checkpoint' or 'stop' playing? > ").lower()
                while True:
                    if game == "checkpoint":
                        print("")
                        player.health += 100
                        blower_room()
                        break
                    elif game == "stop":
                        sys.exit()
                        break
                    else:
                        while game not in ("checkpoint", "stop"):
                            invalid()
                            game = input("\nYou were not able to complete the game. Do you want to go back to your last 'checkpoint' or 'stop' playing? > ").lower()

        #if the player does not have the face mask
        else:
            print("You can't stop coughing, not realizing that the creature is sneakily approaching you. The next thing you know...")
            x()
            print("       YOU WERE KNOCKED OUT")
            x()
            print(".")
            x()
            print(".")
            x()
            print(".")
            x()
            game = input("You were not able to complete the game. Do you want to go back to your last 'checkpoint' or 'stop' playing? > ").lower()
            while True:
                if game == "checkpoint":
                    blower_room()
                elif game == "stop":
                    sys.exit()
                else:
                    while game not in ("checkpoint", "stop"):
                        invalid()
                        game = input("\nYou were not able to complete the game. Do you want to go back to your last 'checkpoint' or 'stop' playing? > ").lower()

    #if the player completed this room
    else:
        print("You remember to use the face mask from before. You quickly put it on to stop coughing. You look around, but there seems to be nothing of importance here.")
        x()

        #continuation of description
        print("The room is still dusty. In the corner of the room, you see a 'box' covered in spider webs and dust. To the 'right', there is a small flap covering a hole. 'Behind' you and to the 'left' are two archways.\n")
        c4 = input("> ").lower()
        while True:
            if c4 == "box":
                if solved['candy'] == True:
                    print("The box is empty.")
                elif solved['motor_room'] == True:
                    print("\nYou remember that the ghost from the Motor Room unlocked something for you. You think it may be this box.")
                    x()
                    print("The box opened! Inside, you find candy?")
                    x()
                    player.inventory['food']['candy'] = 1
                    print("~ New food acquired: candy ~")
                    solved['candy'] = True
                    x()
                    player.health += 100
                    print(f"The candy increases your health to {player.health}.")
                else:
                    print("\nThe box is locked, but you don't see a keyhole. You may need someone's help to open it.")
                c4 = input("> ").lower()
            elif c4 == "right":
                blower_room()
                print("\nYou get on your knees before pulling the flap up and crawling inside.")
                break
            elif c4 == "behind":
                heating_element()
                break
            elif c4 == "left":
                belt_tensioner()
                break
            else:
                while c4 not in ('box', 'right', 'behind', 'left'):
                    invalid()
                    c4 = input("> ").lower()

    return

#Motor Room -
def motor_room():

    #This tells the player where they are.
    print("\nYou are now standing in the Motor Room.")
    x()

    #if the player did not complete the Motor Room
    if solved['motor'] == False:
        print("In the middle of the room, there is a motor. Sitting on the motor is a... um... ghost?")
        x()
        print("              .--,               ")
        print("             /  (                ")
        print("            /    \               ")
        print("           /      \              ")
        print("          /  0  0  \             ")
        print("  ((()   |    ()    |   ()))     ")
        print("  \  ()  (  .____.  )  ()  /     ")
        print("   |` \_/ \  `""`  / \_/ `|      ")
        print("   |       `.'--'.`       |      ")
        print("    \        `""`        /       ")
        print("     \                  /        ")
        print("      `.              .'    ,    ")
        print("       |`             |  _.'|    ")
        print("       |              `-'  /     ")
        print("       \                 .'      ")
        print("        `.____________.-'        ")
        x()
        print("ghost: Hello! I'm Steve! What's your name?")
        x()
        print(f"you: My name is {player.name}.")
        x()
        print("Steve the Ghost: Cool! Wanna be friends?")
        a1 = input("> ").lower()
        while True:
            if a1 == "yes":
                print("\nyou: ...sure..")
                x()
                print("you: but I need to find a way out of this dryer.")
                x()
                print("Steve: ε(´סּ︵סּ`)з  So... you're going to leave me?")
                x()
                print("you: Yes?")
                x()
                print("Steve: I WILL NOT ALLOW THIS! YOU MUST FIGHT ME AND WIN TO BE ABLE TO LEAVE!")
                x()
                break
            elif a1 == "no":
                print("\nyou: Not really. I just want to get out of this dryer.")
                x()
                print("Steve: ٩(╬ʘ益ʘ╬)۶ WHY NOT?!")
                x()
                print("Steve: I WILL NOT ALLOW THIS! YOU MUST FIGHT ME OR YOU SHALL BE STUCK IN THIS ROOM WITH ME FOREVER!")
                x()
                break
            else:
                while a1 not in ("yes", "no"):
                    print("Do you want to be friends with Steve? Enter 'yes' or 'no'.")
                    a1 = input("> ").lower()

        player.stats()
        x()
        ghost.stats()
        x()
        player.battle(ghost)
        x()
        #The game is designed for the player to beat Steve no matter what.
        solved['motor'] = True
        print("Steve faints and you just stare at him on the ground. Ghosts can't die if they're already dead, right?")
        x()
        print("You look around the room and see a piece of gum near the motor. You pick it up.")
        x()
        player.health += 90
        player.inventory['food']['gum'] = 1
        print("~ New food acquired: gum ~")
        x()
        print(f"The gum increases your health to {player.health}.")
        x()
        print("You turn around to leave and see Steve floating back up from the ground.")
        x()
        print("Steve: Are you leaving now?")
        x()
        print("You nod.")
        x()
        print("Steve: ಥ_ಥ At least play a game with me. I promise if you win, I will help you out of this dryer.")
        x()
        print("You: ..okay.")
        x()
        print("Steve: ʘ‿ʘ Yay! Let's play a guessing game. I'm thinking of a number between 0 and 20. You have 10 guesses. What's the number?")
        x()
        guessing_game()
        if solved['motor_room'] == True:
            print("\nSteve: You got it! And like I promised, I'll help you out of the dryer. I just unlocked something for you. (/¯◡ ‿ ◡)/¯")
            x()
        else:
            print("\nSteve: Sorry! You have failed to guess the number in 10 tries. I guess you're stuck here with me. (＾∇＾)")
            x()
            play_again = input("Unless you want to try again? > ").lower()
            while True:
                if play_again == "yes":
                    guessing_game()
                    break
                elif play_again == "no":
                    break
                else:
                    while play_again not in ('yes', 'no'):
                        print("\nDo you want to play again? Enter 'yes' or 'no'.")
                        play_again = input("> ").lower()
        print("Steve: Well, I guess it's time for you to leave me. Good luck!\n")
        #continuation of description
        print("You look around the room. You see Steve just floating around. The motor is in the middle of the room. In 'front' of you, there is an archway.")
        c7 = input("> ").lower()
        while True:
            if c7 == "front":
                blower_room()
                break
            else:
                while c7 != "front":
                    invalid()
                    c7 = input("> ").lower()

    #if the player did not win the guessing game
    elif solved['motor_room'] == False:
        print("Steve: You're back! Do you want to play the game again?")
        c8 = input("> ").lower()
        while True:
            if c8 == "yes":
                guessing_game()
                if solved['motor_room'] == True:
                    print("\nSteve: You got it! And like I promised, I'll help you out of the dryer. I just unlocked something for you. (/¯◡ ‿ ◡)/¯")
                    x()
                else:
                    print("\nSteve: Sorry! You have failed to guess the number in 10 tries. I guess you're stuck here with me. (＾∇＾)")
                    x()
                    play_again_1 = input("Unless you want to try again? > ").lower()
                    while True:
                        if play_again_1 == "yes":
                            guessing_game()
                            break
                        elif play_again_1 == "no":
                            break
                        else:
                            while play_again_1 not in ('yes', 'no'):
                                print("\nDo you want to play again? Enter 'yes' or 'no'.")
                                play_again_1 = input("> ").lower()
                print("Steve: Well, I guess it's time for you to leave me. Good luck!\n")
                #continuation of description
                print("You look around the room. You see Steve just floating around. The motor is in the middle of the room. In 'front' of you, there is an archway.")
                c9 = input("> ").lower()
                while True:
                    if c9 == "front":
                        blower_room()
                        break
                    else:
                        while c9 != "front":
                            invalid()
                            c9 = input("> ").lower()
                break
            elif c8 == "no":
                print("Steve: Well, I guess it's time for you to leave me. Good luck!\n")
                #continuation of description
                print("You look around the room. You see Steve just floating around. The motor is in the middle of the room. In 'front' of you, there is an archway.")
                c10 = input("> ").lower()
                while True:
                    if c10 == "front":
                        blower_room()
                        break
                    else:
                        while c10 != "front":
                            invalid()
                            c10 = input("> ").lower()
                break
            else:
                while c8 not in ("yes", "no"):
                    print("\nDo you want to play? Enter 'yes' or 'no'.")
                    c8 = input("> ").lower()

    #if the player completed the room
    else:
        #continuation of description
        print("You see Steve just floating around the room. There is a motor in the middle of the room. In 'front' of you, there is an archway. There's nothing else for you to see here.")
        c6 = input("> ").lower()
        while True:
            if c6 == "front":
                blower_room()
                break
            else:
                while c6 != "front":
                    invalid()
                    c6 = input("> ").lower()

    return

#Blower Room -
def blower_room():

    print("\n~ checkpoint ~")
    x()

    #This is the description of the room.
    print("You are now standing in the Blower Room. There is a small 'fan' in the middle of the room. In 'front' of you, stairs ascend into darkness. 'Behind' you is an archway. To the 'left', there is a small flap covering a hole.")

    c3 = input("> ").lower()
    while True:
        if c3 == "front":
            print("\nYou begin climbing the stairs. They seem to go on forever...")
            x()
            print(".")
            x()
            print(".")
            x()
            print("...climbing...")
            x()
            print(".")
            x()
            print(".")
            x()
            print("You finally pass through a doorway.")
            x()
            drum_room()
            break
        elif c3 == "fan":
            if solved['open_metal_door'] == False:
                print("\nYou see a metal key attached to a string dangling from one of the fan's blades. You squeeze your hand into the fan and grab the key.")
                x()
                solved['open_metal_door'] = True
                player.inventory['items']['metal key'] = 1
                print("~ New item acquired: metal key ~")
                x()
            else:
                print("\nThere is nothing special about the fan.")
            c3 = input("> ").lower()
        elif c3 == "behind":
            motor_room()
            break
        elif c3 == "left":
            print("\nYou get on your knees before pulling the flap up and crawling inside.")
            x()
            lint_trap()
            break
        else:
            while c3 not in ("front", "behind", "left", "fan"):
                invalid()
                c3 = input("> ").lower()

    return

#Dryer Drum Room - This is the room where the player starts in and where the player will (hopefully) escape the dryer.
def drum_room():

    #This is the description of the room.
    print("You are now in the Dryer Drum Room. The room is dark and cold. It seems to be in the shape of a cylinder. Right behind you is the 'dryer door'. Next to the dryer door, there is a ‘lever’ inside a glass box. In 'front' of you, there is a gap in the wall. To the 'left', there is metal door. To the 'right', stairs descend into darkness.\n")

    c1 = input("> ").lower()
    while True:
        if c1 == "dryer door":
            print("\nThe dryer door is closed and locked. It seems to be connected to the lever.")
            c1 = input("> ").lower()

        elif c1 == "lever":
            if solved['open_lever'] == False:
                print("\nThe box is closed and locked. You cannot get to the lever. However, there is a keyhole.")
                c1 = input("> ").lower()

            #This is the end of the game.
            else:
                print()

                break

        elif c1 == "front":
            heating_duct()
            break

        elif c1 == "left":
            if solved['open_metal_door'] == False:
                print("\nThe door is closed and locked.")
                c1 = input("> ").lower()

            else:
                print("\nThe key fits in the keyhole. The door opens and you walk inside.\n")
                air_flow()
                break

        elif c1 == "right":
            print("\nYou begin walking down the stairs. They seem to go on forever...")
            x()
            print(".")
            x()
            print(".")
            x()
            print("...walking...")
            x()
            print(".")
            x()
            print(".")
            x()
            print("You finally pass through a doorway.")
            x()
            blower_room()
            break

        else:
            while c1 not in ("dryer door", "lever", "front", "left", "right"):
                invalid()
                c1 = input("> ").lower()

    return

#This is the beginning of the game.
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