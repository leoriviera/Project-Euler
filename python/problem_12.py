# Solved correctly
from snippets import divisor_count


def problem_12():
    "What is the value of the first triangle number to have over five hundred divisors?"

    def n_th_triangle(n):
        # Generate the nth triangle number
        return int((n ** 2 + n) / 2)

    n, divisor_total = 3, 0
    # While the total number of divisors is below 500...
    while divisor_total <= 500:
        # Generate the nth triangle number
        triangle = n_th_triangle(n)
        # Find the number of divisors it has
        divisor_total = divisor_count(triangle)
        # Increment n by one
        n += 1

    return triangle


if __name__ == "__main__":
    answer = problem_12()
    print(answer)
