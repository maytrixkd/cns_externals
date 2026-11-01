import random
from math import gcd

def euler_primality_test(n, k=5):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n-1)
        print(f"choosen base : {a}")

        if(gcd(a,n) != 1):
            print("GCD not 1")
            return False

        result = pow(a, (n-1) // 2, n)
        print(f"Euler test result: {result}")

        if(result != 1 and result != n-1):
            return False

    return True

n = int(input("Enter a number: "))

if euler_primality_test(n):
    print(n, "is probably prime")
else:
    print(n, "is composite")