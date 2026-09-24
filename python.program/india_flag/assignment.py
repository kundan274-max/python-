
plaintext = input("\nSender: Enter your message: ")

# Encryption key
key = int(input("Enter encryption key : "))

def encrypt(message, key):
    encrypted_message = ""

    for char in message:
        encrypted_message += chr(ord(char) + key)

    return encrypted_message


def decrypt(message, key):
    decrypted_message = ""

    for char in message:
        decrypted_message += chr(ord(char) - key)

    return decrypted_message

# Encrypt the message
ciphertext = encrypt(plaintext, key)
print("Original Plaintext :", plaintext)
print("Encryption Key     :", key)
print("Ciphertext         :", ciphertext)

print("Intruder sees :", ciphertext)

decrypted_message = decrypt(ciphertext, key)

print("Received Ciphertext:", ciphertext)
print("Decrypted Message  :", decrypted_message)


if plaintext == decrypted_message:
    print("SUCCESS!")
    print("Original message successfully received.")
else:
    print("Decryption Failed!")