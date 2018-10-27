# Solved correctly
# Adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
import random

def is_prime(n):
    for i in range(10):
        a = random.randrange(2, n)
        if pow(a, n-1, n) != 1:
            return False
    return True


def is_cycle_prime(num):
    for i in range(0, len(str(num))):
        if(not is_prime(num)):
            return False
        num = str(num)
        num = num[len(num) - 1] + num[:-1]
        num = int(num.lstrip('0'))
    return True


prime_count = 1
for i in range(3, 1000000, 2):
    if(is_cycle_prime(i)):
        prime_count = prime_count + 1

print(prime_count)
