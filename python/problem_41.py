# Solved correctly
import itertools
import random
from snippets import is_prime


def problem_41():
    "What is the largest n-digit pandigital prime that exists?"

    largest_prime = 0
    perm_string = ''

    for i in range(1, 9 + 1):
        perm_string += str(i)
        for combo in itertools.permutations(perm_string):
            n = int(''.join(combo))

            if (is_prime(n)):
                largest_prime = n

    return largest_prime


if __name__ == "__main__":
    answer = problem_41()
    print(answer)
