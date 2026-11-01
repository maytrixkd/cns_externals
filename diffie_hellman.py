apk = 4
bpk = 3


g = 5
p = 23

A = pow(g, apk, p)
B = pow(g, bpk, p)

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")

sa = pow(B, apk, p)
sb = pow(A, bpk, p)

print(f"Both received {sa} and {sb}")