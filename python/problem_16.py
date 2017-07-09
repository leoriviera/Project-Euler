# Solved correctly
two_to_thousand, total = 2 ** 1000, 0

two_to_thousand_string = str(two_to_thousand)

total = sum(int(digit)for digit in two_to_thousand_string)

print(total)
