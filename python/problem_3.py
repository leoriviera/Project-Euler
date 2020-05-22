import random
import math
from snippets import is_prime


def problem_3():
    "What is the largest prime factor of the number 600851475143?"
    
    n = 600851475143
    largest_factor = 0
    # As we are searching for the largest factor, we can start counting backwards from the floor of the square root of n.
    # The first factor we encounter will be the largest. A detailed explanation can be found at https://en.wikipedia.org/wiki/Primality_test#Simple_methods.
    for i in range(math.floor(math.sqrt(n)), 2, -1):
        # If the number is prime and is a factor of n...
        if(is_prime(i) and n % i == 0):
            # Set the largest factor to i and break.
            largest_factor = i
            break

    return largest_factor


if __name__ == "__main__":
    answer = problem_3()
    print(answer)
