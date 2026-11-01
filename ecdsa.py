import hashlib
import secrets

# Toy curve: y^2 = x^3 + 2x + 2 over F_17.
P = 17
A = 2
B = 2
G = (5, 1)      # base point
N = 19          # order of G
D = 7           # private key


def point_add(p1, p2, p=P, a=A):
    """Add two points on y^2 = x^3 + ax + b modulo p."""
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    x1, y1 = p1
    x2, y2 = p2

    # P + (-P) = point at infinity.
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if p1 == p2:
        # Slope of the tangent line.
        slope = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        # Slope of the secant line.
        slope = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    return (x3, y3)


def point_mul(k, point, p=P, a=A):
    """Double-and-add scalar multiplication."""
    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend, p, a)
        addend = point_add(addend, addend, p, a)
        k >>= 1

    return result


def hash_to_int(message, n=N):
    digest = hashlib.sha256(message.encode()).digest()
    return int.from_bytes(digest, "big") % n


def keygen(d=D, p=P, a=A, g=G):
    return d, point_mul(d, g, p, a)


def sign(message, private_key, p=P, a=A, n=N, g=G):
    d = private_key
    e = hash_to_int(message, n)

    while True:
        k = secrets.randbelow(n - 1) + 1      # 1 <= k <= n - 1
        R = point_mul(k, g, p, a)

        if R is None:
            continue

        r = R[0] % n
        if r == 0:
            continue

        s = (pow(k, -1, n) * (e + d * r)) % n
        if s != 0:
            return (r, s)


def verify(message, signature, public_key, p=P, a=A, n=N, g=G):
    r, s = signature

    if not (0 < r < n and 0 < s < n):
        return False

    e = hash_to_int(message, n)
    w = pow(s, -1, n)
    u1 = (e * w) % n
    u2 = (r * w) % n

    X = point_add(
        point_mul(u1, g, p, a),
        point_mul(u2, public_key, p, a),
        p, a
    )

    if X is None:
        return False

    return X[0] % n == r


if __name__ == "__main__":
    private_key, public_key = keygen()
    message = "hello elliptic curves"

    signature = sign(message, private_key)

    print("Curve: y^2 = x^3 + 2x + 2 mod 17")
    print("Public key Q:", public_key)
    print("On curve:", (public_key[1] ** 2 - public_key[0] ** 3 - A * public_key[0] - B) % P == 0)
    print("Private key d:", private_key)
    print("Signature (r, s):", signature)
    print("Valid signature:", verify(message, signature, public_key))
    print("Tampered message:", verify(message + "!", signature, public_key))