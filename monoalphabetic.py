import string

ALPHABET = string.ascii_uppercase

def encrypt(plaintext, key):
    result = ""

    for char in plaintext.upper():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            result += key[index]
        else:
            result += char

    return result

def decrypt(cipher, key):
    result = ""

    for char in cipher.upper():
        if char in key:
            index = key.index(char)
            result += ALPHABET[index]
        else:
            result += char

    return result

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

message = input("Enter plaintext: ")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
