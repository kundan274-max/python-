numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Two digit numbers are:")

for num in numbers:
    if 10<= abs(num)<=  99:
        print(num)