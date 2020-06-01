from snippets import list_prime_factors
from functools import reduce


def problem_5():
    "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

    num_divisors = []

    # For each divisor between 2 and 20...
    for divisor in range(2, 20 + 1):
        # Get the divisor's prime factors
        prime_factors = list_prime_factors(divisor)
        # Produce a list of unique factors
        unique_factors = set(prime_factors)

        # For each unique factor...
        for factor in unique_factors:
            # Calculate the difference between the count of the
            # factor in the factorisation and the count of the
            # factor in current number prime factorisation
            factor_count_diff = prime_factors.count(
                factor) - num_divisors.count(factor)
            # If the difference is greater than 0...
            # In other words, the number is currently indivisible
            # by the factor in the divisor
            if (factor_count_diff > 0):
                # Add the factor as much as the difference
                num_divisors.extend([factor] * factor_count_diff)

    # Multiply all the divisors together
    num = reduce((lambda x, y: x * y), num_divisors)

    return num


if __name__ == "__main__":
    answer = problem_5()
    print(answer)
