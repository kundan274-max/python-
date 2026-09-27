num = int(input("Enter a 4-digit number: "))

original = num

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10

reverse = d1*1000 + d2*100 + d3*10 + d4

print("Reverse =", reverse)

if original == reverse:
    print("The number is Palindrome.")
else:
    print("The number is Not Palindrome.")