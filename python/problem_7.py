# Solved correctly
import random
import math

# Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
# Determine primailty using the Fermat Primality Test
def is_prime(n):
    if(n == 2):
        return True
    for i in range(50):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True


# Set number of primes to 0.
count = 0
# Start counting primes from 2 (as this is_prime() function cannot handle 1).
n = 2

while True:
    # If the integer n is prime, increase the prime count by 1.
    if(is_prime(n)):
        count += 1
    # If the number of counted primes reaches 10001...
    if(count == 10001):
        # Print the prime and break the while loop.
        print(n)
        break
    # If not, increase integer n by one and repeat.
    n += 1
