def generate_keys(p,g,x):
    y = pow(g,x, p)

    public_key = (p,g,y)
    private_key = x

    return public_key, private_key

def encrypt(message, public_key, k):
    p, g, y = public_key

    c1 = pow(g,k,p)
    c2 = message * pow(y, k, p)

    return c1, c2

def decrypt(cipher, private_key ,p):
    c1, c2 = cipher

    shared_secret = pow(c1, private_key, p)
    inverse = pow(shared_secret, -1, p)

    message = (c2 * inverse) % p

    return message

# Key generation
p = 23
g = 5
x = 6

public_key, private_key = generate_keys(p, g, x)

# Encryption
message = 10
k = 3

ciphertext = encrypt(message, public_key, k)

# Decryption
decrypted_message = decrypt(ciphertext, private_key, p)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)