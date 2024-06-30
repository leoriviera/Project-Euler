# Solved successfully
from functools import reduce
from snippets import list_prime_factors


def problem_47():
    "Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"

    def factors_distinct(factors_lists):
        # Calculate whether two lists of prime factors have distinct entries

        for list in factors_lists:
            prime_factors = set(list)
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
            [previous_prime_factors[0], previous_prime_factors[1], previous_prime_factors[2], current_prime_factors])

        # If they are, break the loop
        if (is_distinct):
            break

        # Remove previous factors
        previous_prime_factors.append(current_prime_factors)
        previous_prime_factors.pop(0)
        # Increment by 1
        n += 1

    result = reduce(lambda a, b: a*b, previous_prime_factors[0])

    return result


if __name__ == "__main__":
    answer = problem_47()
    print(answer)
