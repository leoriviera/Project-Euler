from snippets import is_prime

ceiling = 1_000_000

n = 2
primes = []

while sum(primes) <= ceiling:
    if is_prime(n):
        primes.append(n)

    n += 1


def windows(size, length):
    count = (length - size) + 1

    indexes = []

    for i in range(count):
        indexes.append((i, i + size))

    return indexes


def problem_50():
    length = len(primes)

    for size in range(length, 0 - 1, -1):
        w = windows(size, length)

        sums = map(lambda c: sum(primes[c[0] : c[1]]), w)

        for s in sums:
            if s < ceiling and is_prime(s):
                return s


if __name__ == "__main__":
    answer = problem_50()
    print(answer)
