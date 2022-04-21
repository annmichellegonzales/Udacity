import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def random_monster():
    monster = random.choice(["ogre", "beholder", "dragon"])
    print_pause("You encounter a dangerous " + monster + " !")
    if monster == "dragon":
        print_pause("The red dragon "
                    "menacingly breathes fire "
                    "in your direction.")
    if monster == "ogre":
        print_pause("The ogre bashes his club on the ground.")
    if monster == "beholder":
        print_pause("The beholder's eye "
                    "blinks, and a nearby "
                    "tree gets cut in half.")


def intro():
    print_pause("Welcome, warrior. We do not have time to spare!")
    print_pause("Princess Pinky is in danger, "
                "and it is up to you to rescue her.")
    print_pause("I can only offer you a weapon.")
    print_pause("Jambi presents two weapons for "
                "you to choose. A shiny sword, or "
                "a plain looking mace.")


def choose_weapon():
    choice = valid_input("Choose 1 for sword, or 2 for mace.\n", ['1', '2'])
    if choice == '1':
        print_pause("Excellent choice! This sword is "
                    "imbued with the mystical "
                    "properties of Lake Envalore!")
        print_pause("You receive your weapon, and "
                    "follow Jambi's directions to "
                    "rescue Princes Pinky.")
        random_monster()
        print_pause("You swing your sword, and the monster cowers in fear.")
        print_pause("Another swipe, and it vanishes leaving a pile of dust.")
        print_pause("CONGRATULATIONS! You have rescued Princess Pinky!")
        print_pause("Would you like to play again?")
        # break
        play_again()
    elif choice == '2':
        print_pause("Although this is a fierce mace, it is not enchanted.")
        print_pause("You receive your weapon, and follow Jambi's "
                    "directions to rescue Princes Pinky.")
        random_monster()
        print_pause("You swing your mace, and "
                    "the monster laughs in your face.")
        print_pause("Another swipe, and it's a wipe. "
                    "The monster defeats you in one blow.")
        print_pause("Would you like to play again?")
        # break
        play_again()


def play_again():
    choice = valid_input("Choose 1 for Yes, or 2 for No.\n", ['1', '2'])
    if choice == '1':
        print_pause("Our princess does seem to get herself into "
                    "trouble more often than not. Please rescue her again!")
        play_game()
    elif choice == '2':
        print_pause("Thanks for playing! Good bye.")


def play_game():
    intro()
    choose_weapon()


play_game()
