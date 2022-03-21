import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

print_pause("Welcome, warrior.\n" "We do not have time to spare!")
print_pause("Princess Pinky is in danger, and it is up to you to rescue her.")
print_pause("Please hurry!")
print_pause("I can only offer you a weapon: \n")
print_pause("Jambi presents two weapons for you to choose. A shiny sword, or a plain looking mace")

while True:
    weapon = input("Please enter 1 to choose the sword, or enter 2 to choose the mace.\n")
    if weapon == "1":
        print_pause("Excellent choice! This sword is imbued with the mystical properties of Lake Envalore! \n"
        "You receive your weapon, and follow Jambi's directions to rescue Princes Pinky.")
        break
    elif weapon == "2":
        print_pause("Although this is a fierce mace, it is not enchanted. \n"
        "You receive your weapon, and follow Jambi's directions to rescue Princes Pinky.")
        break
    else:
        print_pause("Enter 1 or 2 to continue.")
