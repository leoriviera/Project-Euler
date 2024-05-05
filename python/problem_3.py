import random
import math
from snippets import list_prime_factors


def problem_3():
    "What is the largest prime factor of the number 600851475143?"

    n = 600851475143

    return max(list_prime_factors(n))


if __name__ == "__main__":
    answer = problem_3()
    print(answer)
