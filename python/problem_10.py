# Solved correctly
from snippets import is_prime


def problem_10():
    "Find the sum of all the primes below two million."

    prime_sum = 2 + sum(filter(is_prime, range(3, 2_000_000, 2)))
    return prime_sum


if __name__ == "__main__":
    answer = problem_10()
    print(answer)
