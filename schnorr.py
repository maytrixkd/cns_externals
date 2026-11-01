import hashlib
import secrets

P = 23
Q = 11
G = 2
X = 6
Y = pow(G,X,P)

def hash_to_challenge(r, message, q=Q):
    data = str(r).encode() + b"|" + message.encode()
    digest = hashlib.sha256(data).digest
    return int.from_bytes(digest, "big") % q

def sign(message, p=P, q=Q, g=G, x=X):
    k = secrets.randbelow(q-1) + 1

    r = pow(g, k, p)
    e = hash_to_challenge(r, message, q)
    s = (k + x * e) % q

    return (e, s)

def verify(message, signature, p=P, q=Q, g=G, y=Y):
    e, s = signature

    if not (0 <= e < q and 0 <= s < q):
        return False

    r = (pow(g, s, p) * pow(y, -e, p)) % p

    return hash_to_challenge(r, message, q) == e
