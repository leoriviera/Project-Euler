# Solved correctly
import random

# Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
# Determine primailty using the Fermat Primality Test
def is_prime(n):
    if(n == 1):
        return False
    if(n == 2):
        return True
    for i in range(50):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True

# Set number of primes, and prime number, to 0
count = 0
prime = 0

# While there are fewer than 10001 primes...
while (count < 10001):
    # Add one to the prime number
    prime += 1
    # If the integer n is prime...
    if(is_prime(prime)):
        # Increase the prime count by 1
        count += 1

print(prime)
