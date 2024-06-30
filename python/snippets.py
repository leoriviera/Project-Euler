from random import randrange, seed
from math import gcd
from collections import Counter
from itertools import chain, repeat, count, islice
from functools import reduce

seed(0)


# Code for repeat_chain, unique_combinations_from_value_counts, unique_combinations from https://stackoverflow.com/a/46623112
def repeat_chain(values, counts):
    return chain.from_iterable(map(repeat, values, counts))


def unique_combinations_from_value_counts(values, counts, r):
    n = len(counts)
    indices = list(islice(repeat_chain(count(), counts), r))
    if len(indices) < r:
        return
    while True:
        yield tuple(values[i] for i in indices)
        for i, j in zip(
            reversed(range(r)), repeat_chain(reversed(range(n)), reversed(counts))
        ):
            if indices[i] != j:
                break
        else:
            return
        j = indices[i] + 1
        for i, j in zip(range(i, r), repeat_chain(count(j), counts[j:])):
            indices[i] = j


def unique_combinations(iterable, r):
    values, counts = zip(*Counter(iterable).items())
    return unique_combinations_from_value_counts(values, counts, r)


def is_abundant(n):
    if sum(list_proper_divisors(n)) > n:
        return True
    return False


def find_triangle_max_path_sum(triangle):
    triangle = list(reversed(triangle))

    previous_line = triangle[0]

    for line_number in range(1, len(triangle)):
        current_line = triangle[line_number]
        calculated_line = []

        for index, integer in enumerate(current_line):
            a = integer + previous_line[index]
            b = integer + previous_line[index + 1]

            if a > b:
                calculated_line.append(a)
            else:
                calculated_line.append(b)

        previous_line = calculated_line

    max_path_sum = previous_line[0]

    return max_path_sum


def is_palindrome(integer):
    # Convert the integer to a string
    string = str(integer)
    # Reverse the string and join it back together
    reversed_string = "".join(reversed(string))
    # If two strings are equal, return true
    if string == reversed_string:
        return True
    # Otherwise, return False
    return False


def is_prime(n):
    # Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
    # Determine primailty using the Fermat Primality Test
    if n == 0 or n == 1:
        return None
    if n == 2:
        return True
    for _ in range(100):
        a = randrange(2, n)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def calculate_smallest_factor(n):
    # Pollard rho Factorisation method adapted from the article at http://mathworld.wolfram.com/PollardRhoFactorizationMethod.html
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n

    while True:
        c = randrange(2, n)

        def f(x):
            return x**2 - c

        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd((x - y) % n, n)
        if d != n:
            return d


def list_prime_factors(n):
    # Generate a list of prime factors for the integer n

    # Start with n on the list
    factors_list = [n]
    # While at least one value is not prime...
    # (While the list isn't empty when filtered with the function not not_prime(f))
    while list(filter(lambda f: (not is_prime(f)), factors_list)) != []:
        # For each factor in the list...
        for factor in factors_list:
            # If the factor is not prime...
            if not is_prime(factor):
                # Find the smallest factor
                factorised = calculate_smallest_factor(factor)
                # Add the factorised factor to the factors list
                factors_list.append(factorised)
                # Add the factor divided by the factorised factor to the factors list
                factors_list.append(int(factor / factorised))
                # Remove the old factor from the list
                factors_list.remove(factor)

    return sorted(factors_list)


def divisor_count(n):
    # Calculate the number of divisors for an integer, n, using prime factorisation

    divisor_count = 1
    if n == 1:
        return 1

    # If n is prime, return 2
    if is_prime(n):
        return 2

    # Return the prime factors of n
    prime_factor_tree = list_prime_factors(n)
    # Find how many times each prime factor occurs
    factors = dict(Counter(prime_factor_tree))
    # For each prime factor in the dictionary of factors
    for base, exponent in factors.items():
        # Multiply the count of the divisors by the exponent + 1
        divisor_count *= exponent + 1

    return divisor_count


def euclidian_algorithm(a, b):
    if a > b:
        a, b = b, a

    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


def simplify_fraction(fraction):
    (numerator, denominator) = fraction

    greatest_common = gcd(numerator, denominator)

    simplified_numerator = int(numerator / greatest_common)
    simplified_denominator = int(denominator / greatest_common)

    return (simplified_numerator, simplified_denominator)


def list_proper_divisors(n):
    if n == 1:
        return []

    prime_factors = list_prime_factors(n)

    factor_combinations = []

    for r in range(1, len(prime_factors)):
        factor_combinations.extend(unique_combinations(prime_factors, r))

    factors_list = [1]

    for combination in factor_combinations:
        factor = reduce((lambda x, y: x * y), combination)
        factors_list.append(factor)

    return set(sorted(factors_list))


def order(a, n):
    p = 0
    while True:
        p += 1
        r = (n**p) % a
        if r == 1:
            return p


def sieve_primes(n):
    sieve = [None] * (n + 1)

    for i in range(2, n):
        # False == None evaluates to True
        # Check if number has been sieved (i.e is False)
        if sieve[i] is False and sieve[i] is not None:
            continue

        if is_prime(i):
            sieve[i] = True

            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    return list(map(lambda p: p[0], filter(lambda p: p[1] == True, enumerate(sieve))))
