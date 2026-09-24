age1 = int(input("Enter age 1: "))
age2 = int(input("Enter age 2: "))
age3 = int(input("Enter age 3: "))

if age1 >= age2 and age1 >= age3:
    print("Oldest age is:", age1)
elif age2 >= age1 and age2 >= age3:
    print("Oldest age is:", age2)
else:
    print("Oldest age is:", age3)