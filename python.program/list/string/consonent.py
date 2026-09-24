s1 = input("Enter any string: ")
s2 = ""
for i in s1:
    if i in "aeiouAEIOU":
        pass
    else:
        s2 = s2 + i

print("Result string =", s2)
