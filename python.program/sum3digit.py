num = int(input("Enter a 3-digit number: "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

sum = digit1 + digit2 + digit3

print("Sum of digits =", sum)