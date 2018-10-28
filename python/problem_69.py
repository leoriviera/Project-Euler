import random, math

# Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
# Determine primailty using the Fermat Primality Test
def is_prime(n):
    if(n == 2):
        return True
    for i in range(10):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True


# Algorithm for printing all prime factors of a n adapted from https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def list_prime_factors(n):
    # Create set to store prime factord
    prime_factors = set()
    # While n is divisible by two...
    while(n % 2 == 0):
        # Add 2 to the set and divide n by 2
        prime_factors.add(2)
        n /= 2

    # For every two integers between 3 and the rounded square root of n...
    for i in range(3, round(math.sqrt(n)) + 1, 2):
        # While n is divisible by i...
        while(n % i == 0):
            # Add i to the set of prime factors and divide by i
            prime_factors.add(i)
            n /= i

    # If n is greater than 2...
    if(n > 2):
        # Add n to the the list of prime factors
        prime_factors.add(int(n))
    
    return list(prime_factors)
        
# Euler's Totient function
def phi(n):
    # If n is a prime, return n - 1
    if(is_prime(n)):
        return n - 1
    # Get a list of prime factors
    prime_factors = list_prime_factors(n)
    # Set the phi value to n
    phi_value = n
    # For each prime factor...
    for factor in prime_factors:
        # Multiply the phi value by 1 minus the inverse of the prime
        phi_value *= (1 - 1 / factor)
    
    # Return the rounded phi value
    return round(phi_value)


max_n, max_ratio = 0, 0
# For each number between n and 2 and 1000000, inclusive...
for n in range(2, 1000000 + 1):
    # Define p as n divided by phi(n)
    ratio = n / phi(n)
    # If n's ratio to p is larger than the max ratio...
    if(ratio >= max_ratio):
        # Set the max ratio to current ratio, and the max n to n
        max_ratio = ratio
        max_n = n

print(max_n)
