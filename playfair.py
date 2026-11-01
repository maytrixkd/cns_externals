def generate_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    characters = []

    for char in key + alphabet:
        if char.isalpha() and char not in characters:
            characters.append(char)

    matrix = [
        characters[i:i + 5]
        for i in range(0, 25, 5)
    ]

    return matrix


def prepare_text(text):
    text = "".join(
        char for char in text.upper()
        if char.isalpha()
    ).replace("J", "I")

    pairs = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            filler = "Q" if first == "X" else "X"
            second = filler
            i += 1

        elif text[i] == text[i + 1]:
            filler = "Q" if first == "X" else "X"
            second = filler
            i += 1

        else:
            second = text[i + 1]
            i += 2

        pairs.append(first + second)

    return pairs


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def playfair_encrypt(plaintext, matrix):
    pairs = prepare_text(plaintext)
    ciphertext = ""

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5]
            ciphertext += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1]
            ciphertext += matrix[(r2 + 1) % 5][c2]

        else:
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]

    return ciphertext


def playfair_decrypt(ciphertext, matrix):
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = "".join(c for c in ciphertext if c.isalpha())

    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext length must be even")

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(matrix, ciphertext[i])
        r2, c2 = find_position(matrix, ciphertext[i + 1])

        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# Main program
key = input("Enter key: ")
matrix = generate_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

plaintext = input("\nEnter plaintext: ")

encrypted = playfair_encrypt(plaintext, matrix)
print("Encrypted text:", encrypted)

decrypted = playfair_decrypt(encrypted, matrix)
print("Decrypted text:", decrypted)