# Solved correctly
import itertools


def problem_43():
    """
    Find the sum of all 0 to 9 pandigital numbers with [sub-string divisibility, where
        digits 2, 3 and 4 are divisible by 2,
        digits 3, 4 and 5 are divisible by 3,
        digits 4, 5 and 6 are divisible by 5,
        digits 5, 6 and 7 are divisible by 7,
        digits 6, 7 and 8 are divisible by 11,
        digits 7, 8 and 9 are divisible by 13 and
        digits 8, 9 and 10 are divisible by 17].
    """

    permutations_list = list(itertools.permutations('0123456789'))
    sub_string_divisors = [2, 3, 5, 7, 11, 13, 17]
    total = 0

    for permutation_index in range(0, len(permutations_list)):
        permutation_sub_strings, append_boolean = [], False

        permutation = permutations_list[permutation_index]

        permutation_string = ''.join(digit for digit in permutation)

        for n in range(0, 7):
            permutation_sub_string = permutation_string[n + 1] + \
                permutation_string[n + 2] + permutation_string[n + 3]
            permutation_sub_strings.append(int(permutation_sub_string))

        for sub_string_index in range(0, 7):
            if permutation_sub_strings[sub_string_index] % sub_string_divisors[sub_string_index] == 0:
                append_boolean = True
            else:
                append_boolean = False
                break

        if append_boolean:
            total += int(permutation_string)

    return total


if __name__ == "__main__":
    answer = problem_43()
    print(answer)
