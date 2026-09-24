s1 = input("enter any string: ")
encrypted = ""

for ch in s1:
    encrypted += chr(ord(ch) + 5)

print("encrypted data =", encrypted)
