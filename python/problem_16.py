# Solved correctly
# Calculate 2^1000 and convert it to a string
two_to_thousand, total = str(2 ** 1000), 0

# Add each of the digits to find the total
total = sum(int(digit) for digit in two_to_thousand)

print(total)
