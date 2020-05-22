# Solved correctly
import math


def problem_53():
    "How many, not necessarily distinct, values of C(n, r) for 1 <= n <=100, are greater than one-million?"

    total = 0

    # For each number, n, between 1 and 100, inclusive...
    for n in range(1, 100 + 1):
        # For each number r, between 1 and n...
        for r in range(1, n + 1):
            # Find the factorials of n, r and the difference between n and r
            n_factorial = math.factorial(n)
            r_factorial = math.factorial(r)
            n_minus_r_factorial = math.factorial(n - r)

            # Calculate n_C_r by dividing n! by (r! - (n-r)!)
            n_C_r = n_factorial / (r_factorial * n_minus_r_factorial)
            # If n_C_r is greater than 1000000, add 1 to the total
            if n_C_r > 1000000:
                total += 1

    return total


if __name__ == "__main__":
    answer = problem_53()
    print(answer)
