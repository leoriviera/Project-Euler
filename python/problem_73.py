from snippets import list_proper_divisors
from decimal import Decimal


def problem_73():

    fractions = []

    proper_divisors = {}

    ceiling = 12_000

    for d in range(2, ceiling + 1):
        proper_divisors[d] = list_proper_divisors(d)

        fractions.append(Decimal(1) / Decimal(d))
        for n in range(2, d):
            has_common_factor = len(
                proper_divisors[d].intersection(proper_divisors[n])) > 1

            if(not has_common_factor and n not in proper_divisors[d]):
                fractions.append(Decimal(n) / Decimal(d))

    sorted_fractions = sorted(fractions)

    third_index = sorted_fractions.index(Decimal(1) / Decimal(3))
    half_index = sorted_fractions.index(Decimal(1) / Decimal(2))

    return half_index - third_index - 1


if __name__ == "__main__":
    answer = problem_73()
    print(answer)
