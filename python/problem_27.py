from snippets import is_prime


def problem_27():
    "Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0."

    max_a, max_b = 0, 0
    max_consecutive_prime = 0

    for a in range(-1000, 1000 + 1):
        for b in range(-999, 1000):
            n = 0
            while True:
                n_squared = n ** 2
                quadratic_result = n_squared + (a * n) + b
                if is_prime(abs(quadratic_result)):
                    n += 1
                elif n > max_consecutive_prime:
                    max_consecutive_prime = n
                    max_a, max_b = a, b
                    break
                else:
                    break

    product = max_a * max_b

    return product


if __name__ == "__main__":
    answer = problem_27()
    print(answer)
