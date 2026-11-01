from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(
    key_size=2048
)

public_key = private_key.public_key()

message = b"Sample"

sign = private_key.sign(
    message, hashes.SHA256()
)

try:
    public_key.verify(
        sign, message, hashes.SHA256()
    )
    print("Valid")

except InvalidSignature:
    print("Invalid")