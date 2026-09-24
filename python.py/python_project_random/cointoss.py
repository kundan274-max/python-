import random

choices = ["head", "tail"]

computer = random.choice(choices)

user = input("Choose Head or Tail: ").lower()

print("Coin result:", computer)

if user == computer:
    print("Congratulations! You guessed correctly.")

else:
    print("Wrong guess!")