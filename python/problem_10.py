# Solved correctly
from snippets import sieve_primes


def problem_10():
    "Find the sum of all the primes below two million."

    prime_sum = sum(sieve_primes(2_000_000))
    return prime_sum


if __name__ == "__main__":
    answer = problem_10()
    print(answer)
