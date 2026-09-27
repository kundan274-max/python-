import random

while True:

    choice = input("Press Enter to roll the dice or q to quit: ")

    if choice == "q":
        print("Game Over!")
        break

    dice = random.randint(1, 6)

    print("You rolled:", dice)