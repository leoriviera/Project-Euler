from snippets import is_prime


def problem_58():
    "Starting with 1 and spiralling anticlockwise, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?"

    corner_n = 1
    prime_proportion = 1

    prime_count = 0
    total = 1

    loop_count = 1
    side_length = 1

    while prime_proportion > 0.1:

        for i in range(1, 4 + 1):
            corner_n += 2 * loop_count

            total += 1

            if (is_prime(corner_n)):
                prime_count += 1

        loop_count += 1
        side_length += 2

        prime_proportion = prime_count / total

    return side_length


if __name__ == "__main__":
    answer = problem_58()
    print(answer)
