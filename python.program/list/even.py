num1 = []

for i in range(10):
    num = int(input("Enter number: "))
    num1.append(num)

print("Even numbers are:")

for num in num1:
    if num % 2 == 0:
        print(num)
