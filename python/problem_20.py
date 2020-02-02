# Solved correctly
import math

# Calculate 100! and convert to a string
one_hundred_bang = str(math.factorial(100))

# Calculate the sum of the digits in the string
total = sum(int(digit) for digit in one_hundred_bang)

print(total)
