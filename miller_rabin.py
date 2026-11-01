import random
from math import gcd

def miller_rabin(n, k=5):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    d =n-1
    s = 0;

    while d % 2 == 0:
        d //= 2
        s += 1

    print(f"Calculated s = {s} and d = {d}")

    for _ in range(k):
        a = random.randint(2, n-2)
        print(f"Choosen base = {a}")

        if(gcd(a, n) != 1):
            return False

        x = pow(a, d, n)
        print(f"Calculated x = {x}")

        if x == 1 or x == n-1:
            continue

        print("Entering inner loop")
        for _ in range(s-1):
            x = pow(x, 2, n)
            print(f"Calculated inner x = {x}")

            if x == n-1:
                break
        else:
            return False

    return True

n = int(input("Enter a number: "))

if miller_rabin(n):
    print(n, "is probably prime")
else:
    print(n, "is composite")