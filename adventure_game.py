import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def intro():
    print_pause("Welcome, warrior. We do not have time to spare!")
    print_pause("Princess Pinky is in danger, and it is up to you to rescue her.")
    print_pause("I can only offer you a weapon: ")
    print_pause("Jambi presents two weapons for you to choose. A shiny sword, or a plain looking mace.")

def choose_weapon():
    choice = input("Please enter 1 to choose the sword, or enter 2 to choose the mace.\n")
    if choice == 1:
        print_pause("Excellent choice! This sword is imbued with the mystical properties of Lake Envalore!")
    elif choice == 2:
        print_pause("Although this is a fierce mace, it is not enchanted.")
    else:
        print_pause("Please save her!")
        return choice


intro()
while True:

    choose_weapon()
    print_pause("You receive your weapon, and follow Jambi's directions to rescue Princes Pinky.")
    play_again = valid_input("Would you like to play again? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in play_again:
        print_pause("Thanks for playing! Good bye.")
        break
    elif "yes" in play_again:
        print_pause("Our princess does seem to get herself into trouble more often than not. Please rescue her again!")