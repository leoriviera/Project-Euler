# Solved correctly
import itertools

permutations_list = list(itertools.permutations('0123456789'))
millionth_permutation = permutations_list[1000000 - 1]
millionth_permutation_string = ''

millionth_permutation_string = ''.join(
    digit for digit in millionth_permutation)

print(millionth_permutation_string)
