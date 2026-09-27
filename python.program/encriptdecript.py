def encrypt(text, key):
    encrypted = ""

    for char in text:
        encrypted += chr(ord(char) + key)

    return encrypted


def decrypt(text, key):
    decrypted = ""

    for char in text:
        decrypted += chr(ord(char) - key)

    return decrypted

text = input("Enter any string: ")
key = int(input("Enter encryption key: "))

encrypted_text = encrypt(text, key)

print("\nEncrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)

print("Decrypted Text:", decrypted_text)