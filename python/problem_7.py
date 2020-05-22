# Solved correctly
from snippets import is_prime


def problem_7():
    "What is the 10001st prime number?"

    # Set number of primes to 2 (counting 2 and 3)
    count = 2
    # Set initial n to 3
    n = 3

    # While there are fewer than 10001 primes...
    while (count < 10001):
        # Add two
        n += 2
        # If the integer n is prime...
        if(is_prime(n)):
            # Increase the prime count by 1
            count += 1

    return n


if __name__ == "__main__":
    answer = problem_7()
    print(answer)
