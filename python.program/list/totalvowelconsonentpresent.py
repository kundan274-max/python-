s1 = input("Enter any string: ")
c = 0
v = 0

for i in s1:
    if i in "aeiouAEIOU":
        v = v + 1
    else:
        c = c + 1

print("Total consonants =", c)
print("Total vowels =", v)
