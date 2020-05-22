import random
import math
import collections


def find_triangle_max_path_sum(triangle):
    triangle = list(reversed(triangle))

    previous_line = triangle[0]

    for line_number in range(1, len(triangle)):

        current_line = triangle[line_number]
        calculated_line = []

        for index, integer in enumerate(current_line):
            a = integer + previous_line[index]
            b = integer + previous_line[index + 1]

            if (a > b):
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
    reversed_string = ''.join(reversed(string))
    # If two strings are equal, return true
    if(string == reversed_string):
        return True
    # Otherwise, return False
    return False


def is_prime(n):
    # Primality test adapted from the Brilliant.org wiki entry on primality testing, found at https://brilliant.org/wiki/prime-testing/
    # Determine primailty using the Fermat Primality Test
    if (n == 0 or n == 1):
        return None
    if(n == 2):
        return True
    for i in range(75):
        a = random.randrange(2, n)
        if(pow(a, n-1, n) != 1):
            return False
    return True


def calculate_smallest_factor(n):
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
                # Find the samllest factor
                factorised = calculate_smallest_factor(factor)
                # Add the factorised factor to the factors list
                factors_list.append(factorised)
                # Add the factor divided by the factorised factor to the factors list
                factors_list.append(int(factor / factorised))
                # Remove the old factor from the list
                factors_list.remove(factor)

    return factors_list


def divisor_count(n):
    # Calculate the number of divisors for an integer, n, using prime factorisation

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
