score = 0

print("Welcome to Kundan Quiz!")

answer = input("What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1

else:
    print("Wrong!")

answer = input("Who developed Python? ")

if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1

else:
    print("Wrong!")
    answer = input("Father of History ")

if answer.lower() == "Herodotus":
    print("Correct!")
    score += 1

else:
    print("Wrong!")
    answer = input("battele of Palasi  ")

if answer.lower() == "1757":
    print("Correct!")
    score += 1

else:
    print("Wrong!")

print("Your total score is:", score)
