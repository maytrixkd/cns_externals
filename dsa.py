import hashlib
import secrets

# Toy domain parameters.
P = 23          # large prime (tiny here)
Q = 11          # prime divisor of P - 1
G = 2           # element of order Q modulo P
X = 6           # private key
Y = pow(G, X, P)  # public key


def hash_to_int(message, q=Q):
    digest = hashlib.sha256(message.encode()).digest()
    return int.from_bytes(digest, "big") % q


def sign(message, p=P, q=Q, g=G, x=X):
    h = hash_to_int(message, q)

    while True:
        k = secrets.randbelow(q - 1) + 1      # 1 <= k <= q - 1
        r = pow(g, k, p) % q

        if r == 0:
            continue

        s = (pow(k, -1, q) * (h + x * r)) % q

        if s != 0:
            return (r, s)


def verify(message, signature, p=P, q=Q, g=G, y=Y):
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    h = hash_to_int(message, q)
    w = pow(s, -1, q)
    u1 = (h * w) % q
    u2 = (r * w) % q

    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r


if __name__ == "__main__":
    message = "hello dsa"
    signature = sign(message)

    print("Public key (p, q, g, y):", (P, Q, G, Y))
    print("Private key x:", X)
    print("Signature (r, s):", signature)
    print("Valid signature:", verify(message, signature))
    print("Tampered message:", verify(message + "!", signature))