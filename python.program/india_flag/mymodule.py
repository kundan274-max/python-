def add(a, b):
    return a + b


from mymodule import add

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", add(a, b))