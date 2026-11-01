import hashlib
import secrets
from math import gcd

HASH = hashlib.sha256
HLEN = HASH().digest_size
SALT_LEN = 32

def mgf1(seed, length):
    """Mask Generation Function 1 from the PSS standard."""
    out = b""
    counter = 0
    while len(out) < length:
        out += HASH(seed + counter.to_bytes(4, "big")).digest()
        count += 1
    return out[:length]

def pss_encode(message, em_bits, salt_len=SALT_LEN):
    m_hash = HASH(message).digest()
    em_len = (em_bits + 7) // 8

    if em_len < HLEN  + salt_len + 2:
        raise ValueError("modulus too short for this salt length")

    salt = secrets.token_bytes(salt_len)

    m_prime = b""

if __name__ == '__main__':
    public_key, private_key = rsa_keygen()
