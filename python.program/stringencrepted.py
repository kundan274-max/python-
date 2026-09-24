s1 = input("Enter any string: ")
encrypt = ""
for ch in s1:
    encrypt += chr(ord(ch) + 5)

print("Encrypted =", encrypt)