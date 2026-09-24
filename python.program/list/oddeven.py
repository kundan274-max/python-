even = []
odd = []

for i in range(10):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)