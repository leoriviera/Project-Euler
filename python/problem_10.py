# Solved correctly
import random
import math
from snippets import is_prime


def problem_10():
    "Find the sum of all the primes below two million."
    
    # Create a list of primes with the value 2
    # This will allow the loop to start at 3, and step by 2
    primes = [2]

    # For all odd integers between 3 and 2000000
    for i in range(3, 2000000, 2):
        # If the integer is prime, append to the prime list
        if(is_prime(i)):
            primes.append(i)

    answer = sum(primes)

    return answer


if __name__ == "__main__":
    answer = problem_10()
    print(answer)
