import hashlib
import secrets
from math import gcd

P = 23
G = 5
X = 6
Y = pow(G,X,P)

def hash_to_int(message, modulus):
    digest = hashlib.sha256(message.encode()).digest()
    return int.from_bytes(digest, "big") % modulus

def sign(message, p=P, g=G, x=X):
    h = hash_to_int(message, p-1)

    while(True):
        k = secrets.randbelow(p-2) + 1
        if gcd(k, p-1) != 1:
            continue

        r = pow(g, k, p)
        s = (pow(k, -1, p-1) * (h - x * r)) % (p-1)

        if s != 0:
            return (r, s)

def verify(message, signature, p=P, g=G, y=Y):
    r, s = signature

    if not (0 < r < p):
        return False

    h = hash_to_int(message, p-1)
    left = (pow(y, r, p) * pow(r, s, p)) % p
    right = pow(g, h, p)

    return left == right

if __name__ == "__main__":
    message = "hello elgamal signature"
    signature = sign(message)

    print("Public key (p, g, y):", (P, G, Y))
    print("Private key x:", X)
    print("Signature (r, s):", signature)
    print("Valid signature:", verify(message, signature))
    print("Tampered message:", verify(message + "!", signature))