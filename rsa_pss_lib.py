from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature

pk = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

pss = padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()),
    salt_length=32
)

public_key = pk.public_key()

message = b"This is something sample"

sign = pk.sign(
    message, pss, hashes.SHA256()
)

r, s = decode_dss_signature(sign)
print(f"{r} {s}")

try:
    public_key.verify(
        sign, message, pss, hashes.SHA256()
    )
    print("Valid")
except InvalidSignature:
    print('Invalid')

