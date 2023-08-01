from snippets import is_palindrome, is_prime


def problem_808():

    def reverse_number(n):
        reversed_n = str(n)[::-1]
        return int(reversed_n.lstrip('0'))

    reversible_prime_squares = []

    n = 12

    while len(reversible_prime_squares) < 50:
        n += 1

        if n in reversible_prime_squares:
            continue

        if(str(n)[-1] == '0'):
            continue

        if(is_palindrome(n)):
            continue

        reversed_n = reverse_number(n)

        if(is_prime(n) and is_prime(reversed_n)):
            n_squared = n * n
            reversed_n_squared = reversed_n * reversed_n

            if(n_squared == reverse_number(reversed_n_squared)):
                reversible_prime_squares.extend((n, reversed_n))

    return sum(map(lambda x: x * x, reversible_prime_squares))


if __name__ == "__main__":
    answer = problem_808()
    print(answer)
