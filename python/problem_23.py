from itertools import combinations_with_replacement
from snippets import is_abundant


def problem_23():
    "Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."
    ceiling = 28123

    abundant_numbers = list(filter(is_abundant, range(1, (ceiling + 1))))

    abundant_pair_sum_combinations = combinations_with_replacement(
        abundant_numbers, 2)

    abundant_pair_numbers = set(map(sum, abundant_pair_sum_combinations))

    non_abundant_pair_numbers = filter(
        lambda x: x not in abundant_pair_numbers, range(1, ceiling + 1))

    answer = sum(non_abundant_pair_numbers)

    return answer


if __name__ == "__main__":
    answer = problem_23()
    print(answer)
