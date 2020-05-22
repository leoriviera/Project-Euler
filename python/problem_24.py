import itertools


def problem_24():
    "What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"

    # Create a list of permutations of the numbers 0 to 9.
    permutations_list = list(itertools.permutations('0123456789'))
    # Find the millionth permutation in the list
    millionth_permutation = permutations_list[1000000 - 1]
    # Join the digits in the millionth permutation
    millionth_permutation_string = ''.join(
        digit for digit in millionth_permutation)

    return millionth_permutation_string


if __name__ == "__main__":
    answer = problem_24()
    print(answer)
