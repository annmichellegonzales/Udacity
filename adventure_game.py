import time

# create function, example of print_pause
# def print_pause():
#     time.sleep(2) + print

print("Welcome, warrior.\n" "We do not have time to spare!")
time.sleep(2)
print("Princess Pinky is in danger, and it is up to you to rescue her.")
time.sleep(2)
print("Please hurry!")
time.sleep(1)
print("I can only offer you a weapon: \n")
print("Jambi presents two weapons for you to choose.")

while True:
    weapon = input("Please enter 1 to choose the sword, or enter 2 to choose the mace.\n")
    if weapon == "1":
        print("Excellent choice! This sword is imbued with the mystical properties of Lake Envalore! \n"
        "You receive your weapon, and follow Jambi's directions to rescue Princes Pinky.")
        break
    elif weapon == "2":
        print("Although this is a fierce mace, it is not enchanted. \n"
        "You receive your weapon, and follow Jambi's directions to rescue Princes Pinky.")
        break
    else:
        print("Enter 1 or 2 to continue.")
