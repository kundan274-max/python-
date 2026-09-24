# Caesar Cipher - Encryption and Decryption

text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted = ""

for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        encrypted += chr((ord(char) - base + shift) % 26 + base)
    else:
        encrypted += char

print("Ciphertext:", encrypted)


# Decryption
decrypted = ""

for char in encrypted:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        decrypted += chr((ord(char) - base - shift) % 26 + base)
    else:
        decrypted += char

print("Decrypted Text:", decrypted)