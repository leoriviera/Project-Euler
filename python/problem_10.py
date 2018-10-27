# Solved correctly
import random, math

# Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
# Determine primailty using the Fermat Primality Test
def is_prime(n):
    if(n == 2):
        return True
    for i in range(100):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True

# Create a list of primes with the value 2
# This will allow the loop to start at 3, and step by 2
primes = [2]

# For all odd (step-2) integers between 3 and 2000000
for i in range(3, 2000000, 2):
    # If the integer is prime, append to the prime list
    if(is_prime(i)):
        primes.append(i)

answer = sum(primes)

print(answer)
