def hill_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")

    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        p1 = ord(plaintext[i]) - ord('A')
        p2 = ord(plaintext[i+1]) - ord('A')
        print(f"{p1}, {p2}")

        c1 = (key[0][0] * p1 + key[0][1] * p2)
        c2 = (key[1][0] * p1 + key[1][1] * p2)
        print(f"Before modulo : {c1}, {c2}")
        c1 = c1 % 26
        c2 = c2 % 26
        print(f"After modulo: {c1}, {c2}")

        ciphertext += chr(c1 + ord('A'))
        ciphertext += chr(c2 + ord('A'))

    return ciphertext

def hill_decrypt(ciphertext, inverse_key):
    ciphertext = ciphertext.upper().replace(" ", "")

    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext length must be even")

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        c1 = ord(ciphertext[i]) - ord('A')
        c2 = ord(ciphertext[i + 1]) - ord('A')

        p1 = (inverse_key[0][0] * c1 +
              inverse_key[0][1] * c2) % 26

        p2 = (inverse_key[1][0] * c1 +
              inverse_key[1][1] * c2) % 26

        plaintext += chr(p1 + ord('A'))
        plaintext += chr(p2 + ord('A'))

    return plaintext


inverse_key = [
    [15, 17],
    [20, 9]
]

key = [
    [3,3],
    [2,5]
]

plaintext = input("Enter plaintext: ")
ciphertext = hill_encrypt(plaintext, key)

print("Encrypted: ", ciphertext)
ciphertext = input()
print("Decrypted text:", hill_decrypt(ciphertext, inverse_key))