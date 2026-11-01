def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result

word = input("Enter the word")
print(f"{word} encrypted to {encrypt(word, 1)}")
