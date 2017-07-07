# Solved correctly
import itertools

permutations_list = list(itertools.permutations('0123456789'))
print(len(permutations_list))
sub_string_divisors = [2, 3, 5, 7, 11, 13, 17]
total = 0

for permutation_index in range(0, len(permutations_list)):
    permutation_sub_strings, append_boolean = [], False

    permutation = permutations_list[permutation_index]
    permutation_string = ''

    for digit_index in range(0, len(permutation)):
        permutation_string += permutation[digit_index]

    for n in range(0, 7):
        permutation_sub_string = permutation_string[n + 1] + permutation_string[n + 2] + permutation_string[n + 3]
        permutation_sub_strings.append(int(permutation_sub_string))

    for sub_string_index in range(0, 7):
        if permutation_sub_strings[sub_string_index] % sub_string_divisors[sub_string_index] == 0:
            append_boolean = True
        else:
            append_boolean = False
            break

    if append_boolean:
        total += int(permutation_string)

print(total)
