def encrypt(plain, key):
    result = ""

    key = key.upper()
    j = 0

    for char in plain.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')

            c = (p+k) % 26
            result += chr(c + ord('A'))
            j += 1
        else:
            result += char

    return result

def decrypt(cipher, key):
    result = ""
    key = key.upper()
    j = 0

    for char in cipher.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')

            p = (c-k) % 26
            result += chr(p + ord('A'))
            j += 1

        else:
            result += char

    return result

message = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(message, key)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypt(ciphertext, key))