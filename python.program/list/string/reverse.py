s1 = input("Enter any string: ")
s2 = ""

for i in range(len(s1) - 1, -1, -1):
    s2 += s1[i]

print("Reversed string =", s2)