# Solved correctly
from snippets import is_prime


def problem_10():
    "Find the sum of all the primes below two million."

    # Create a list of primes with the value 2
    # This will allow the loop to start at 3, and step by 2
    prime_sum = 0

    # For all odd integers between 3 and 2000000
    for i in range(3, 2_000_000, 2):
        # If the integer is prime, append to the prime list
        if is_prime(i):
            prime_sum += i

    return prime_sum


if __name__ == "__main__":
    answer = problem_10()
    print(answer)
