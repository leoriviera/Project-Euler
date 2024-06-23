from snippets import is_prime, order


def problem_26():
    primes = filter(is_prime, range(10, 1000))

    n = map(lambda p: (p, order(p, 10)), primes)

    (d, _) = max(n, key=lambda pair: pair[1])

    return d


if __name__ == "__main__":
    answer = problem_26()
    print(answer)
