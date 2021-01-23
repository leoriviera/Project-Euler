import random
import math
from snippets import is_prime, list_prime_factors


def problem_69():
    "Find the value of n <= 1,000,000 for which n/φ(n) is a maximum, where φ(n) is Euler's Totient function."

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

    return max_n


if __name__ == "__main__":
    answer = problem_69()
    print(answer)
