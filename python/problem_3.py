# Solved correctly
import random, math

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


n = 600851475143
largest_factor = 0
# As we are searching for the largest factor, we can start counting backwards from the floor of the square root of n.
# The first factor we encounter will be the largest. A detailed explanation can be found at https://en.wikipedia.org/wiki/Primality_test#Simple_methods.
for i in range(math.floor(math.sqrt(n)), 2, -1):
    # If the number is prime and is a factor of n...
    if(is_prime(i) and n % i == 0):
        # Set the largest factor to i and break.
        largest_factor = i
        break

print(largest_factor)
