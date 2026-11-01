from math import gcd

def generate_keys(p,q,e):
    n = p * q
    phi = (p-1) * (q-1)

    if not (1 < e < phi) or gcd(e, phi) != 1:
        raise ValueError("Invalid public exponent")

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key

    if not (0 <= message < n):
        raise ValueError("Invalid public exponent")

    return pow(message, e, n)

def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

p = 7
q = 13
e = 5
public_key, private_key = generate_keys(p,q,e)

message = 10
ciphertext = encrypt(message, public_key)

decrypted_message = decrypt(ciphertext, private_key)

print(f"Public Key: {public_key}")
print("Private Key:", private_key)
print("Original Message:", message)
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted_message)