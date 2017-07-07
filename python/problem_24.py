# Solved correctly
import itertools

permutations_list = list(itertools.permutations('0123456789'))
millionth_permutation = permutations_list[1000000 - 1]
millionth_permutation_string = ''

for digit_index in range(0, len(millionth_permutation)):
    millionth_permutation_string += millionth_permutation[digit_index]

print(millionth_permutation_string)
