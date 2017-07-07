# Solved correctly
two_to_thousand, total = 2 ** 1000, 0

two_to_thousand_string = str(two_to_thousand)

for digit_index in range(0, len(two_to_thousand_string)):
    digit_int = int(two_to_thousand_string[digit_index])
    total += digit_int

print(total)
