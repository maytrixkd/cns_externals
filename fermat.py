import random
from math import gcd

def fermat_primality_test(n, k = 5):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n-1)

        if (gcd(a, n) != 1):
            return False

        if(pow(a, n-1, n) != 1):
            return False

    return True

n = int(input('Enter a number: '))

if fermat_primality_test(n):
    print(f"{n} is probably prime")
else:
    print(f"{n} is not a prime")