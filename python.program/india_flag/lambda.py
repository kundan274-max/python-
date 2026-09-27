# Average of three numbers using lambda

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = lambda x, y, z: (x + y + z) / 3

print("Average =", average(a, b, c))