# Solved correctly
import random
import math
import fractions
import collections

# More information about calculating divisors using prime factorisation can be found at http://www.gmathacks.com/gmat-math/number-of-factors-of-a-large-integer.html
# Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
# Determine primailty using the Fermat Primality Test
def is_prime(n):
    if(n == 1):
        return True
    if(n == 2):
        return True
    for i in range(10):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True

# Pollard rho Factorisation method adapted from the article at http://mathworld.wolfram.com/PollardRhoFactorizationMethod.html
def is_factorised(n):
    if(n % 2 == 0):
        return 2
    while True:
        c = random.randrange(2, n)

        def f(x): return (x**2 - c)
        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = fractions.gcd((x - y) % n, n)
        if(d != n):
            return d


# Generate a list of prime factors for the integer n
def list_prime_factors(n):
    # Start with n on the list
    factors_list = [n]
    # While at least one value is not prime...
    # (While the list isn't empty when filtered with the function not not_prime(f))
    while (list(filter(lambda f: (not is_prime(f)), factors_list)) != []):
        # For each factor in the list...
        for factor in factors_list:
            # If the factor is not prime...
            if(not is_prime(factor)):
                # Factorise the factor further
                factorised = is_factorised(factor)
                # Add the factorised factor to the factors list
                factors_list.append(factorised)
                # Add the factor divided by the factorised factor to the factors list
                factors_list.append(int(factor / factorised))
                # Remove the old factor from the list
                factors_list.remove(factor)

    return factors_list


# Calculate the number of divisors for an integer, n, using prime factorisation
def divisor_counter(n):
    divisor_count = 1
    # If n is prime, return 2
    if(is_prime(n)):
        return 2

    # Return the prime factors of n
    prime_factor_tree = list_prime_factors(n)
    # Find how many times each prime factor occurs
    factors = dict(collections.Counter(prime_factor_tree))
    # For each prime factor in the dictionary of factors
    for base, exponent in factors.items():
        # Multiply the count of the divisors by the exponent + 1
        divisor_count *= (exponent + 1)

    return divisor_count


# Generate the nth triangle number
def n_th_triangle(n):
    return int((n ** 2 + n) / 2)


n, divisor_total = 3, 0
# While the total number of divisors is below 500...
while divisor_total <= 500:
    # Generate the nth triangle number
    triangle = n_th_triangle(n)
    # Find the number of divisors it has
    divisor_total = divisor_counter(triangle)
    # Increment n by one
    n += 1

print(triangle)
