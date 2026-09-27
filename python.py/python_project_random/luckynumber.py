import random

lucky_number = random.randint(1, 10)

user_number = int(input("Enter a number between 1 and 10: "))

if user_number == lucky_number:

    print("Congratulations! You won!")

else:

    print("Sorry! You lost!")

print("Lucky number was:", lucky_number)