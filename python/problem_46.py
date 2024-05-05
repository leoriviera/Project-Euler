import math
from snippets import is_prime


def problem_46():
    n = 3

    while True:
        # If n is prime, increment and skip
        if is_prime(n):
            n += 2
            continue

        # Calculate the maximum possible square
        c = math.floor(math.sqrt(n / 2))
        # For each number between 0 and the ceiling,
        # calculate double the square, subtract n, and
        # determine if the difference is prime
        q = any([is_prime(n - 2 * (m**2)) for m in range(0, c + 1)])

        # If the difference is prime, Goldbach's conjecture holds
        # and we increment, otherwise return n
        if q:
            n += 2
        else:
            return n


if __name__ == "__main__":
    answer = problem_46()
    print(answer)
