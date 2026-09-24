#Assignment 1 
plaintext = 85
print("----- SENDER SIDE -----")
print("Original Plaintext:", plaintext)
ciphertext = plaintext - 40
print("Encrypted Ciphertext:", ciphertext)
print("\n----- INTRUDER SIDE -----")
print("Intruder sees:", ciphertext)
print("\n----- RECEIVER SIDE -----")
decrypted_text = ciphertext + 40
print("After Decryption:", decrypted_text)