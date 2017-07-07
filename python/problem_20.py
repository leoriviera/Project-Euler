# Solved correctly
import math as maths

one_hundred_bang, total = maths.factorial(100), 0

one_hundred_bang_string = str(one_hundred_bang)

for digit_index in range(0, len(one_hundred_bang_string)):
    digit_int = int(one_hundred_bang_string[digit_index])
    total += digit_int

print(total)
