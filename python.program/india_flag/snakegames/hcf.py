n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
i=1
while i <= n1 and i <= n2:
    if n1 % i == 0 and n2 % i == 0:
        hcf = i
    i += 1
print("Greatest Common Divisor:", hcf)