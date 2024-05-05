import itertools
from snippets import is_prime


def problem_49():
    r = range(1000, 9999 + 1)

    primes = list(filter(is_prime, r))

    sequences = []

    for n in primes:
        permutations = map(lambda p: int("".join(p)), itertools.permutations(str(n), 4))

        intersection = sorted(set(permutations).intersection(set(primes)))

        if len(intersection) >= 3 and (not any([n in s for s in sequences])):
            sequences.extend(list(itertools.combinations(intersection, 3)))

    prime_permutations = []

    for sequence in sequences:
        a, b, c = sequence

        if (c - b) == (b - a):
            prime_permutations.append(sequence)

    return "".join([str(i) for i in prime_permutations[1]])


if __name__ == "__main__":
    answer = problem_49()
    print(answer)
