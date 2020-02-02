# Solved successfully
import random
import math
from functools import reduce

def is_prime(n):
    # Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
    # Determine primailty using the Fermat Primality Test
    if(n == 1):
        return True
    if(n == 2):
        return True
    for i in range(10):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True


def is_factorised(n):
    # Pollard rho Factorisation method adapted from the article at http://mathworld.wolfram.com/PollardRhoFactorizationMethod.html
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
            d = math.gcd((x - y) % n, n)
        if(d != n):
            return d


def list_prime_factors(n):
    # Generate a list of prime factors for the integer n

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


def factors_distinct(*args):
    # Calculate whether two lists of prime factors have distinct entries

    for arg in args:
        prime_factors = set(arg)
        if (len(prime_factors) != 4):
            return False
    return True


# Start with prime factors of 2, 3 and 4, with n = 5
previous_prime_factors = [[2], [3], [2, 2]]
n = 5

while True:
    # List the current number's prime factors
    current_prime_factors = list_prime_factors(n)
    # Find whether the current and previous factors are distinct
    is_distinct = factors_distinct(
        previous_prime_factors[0], previous_prime_factors[1], previous_prime_factors[2], current_prime_factors)

    # If they are, break the loop
    if (is_distinct):
        break

    # Remove previous factors
    previous_prime_factors.append(current_prime_factors)
    previous_prime_factors.pop(0)
    # Increment by 1
    n += 1

result = reduce(lambda a, b: a*b, previous_prime_factors[0])

print(result)
