# Solved correctly
import math

one_hundred_bang, total = math.factorial(100), 0

one_hundred_bang_string = str(one_hundred_bang)

total = sum(int(digit) for digit in one_hundred_bang_string)

print(total)
