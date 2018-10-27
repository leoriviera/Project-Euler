# Solved correctly
import math

# For a in the range between 1 and 1000...
for a in range(1, 1000):
    # Find a squared.
    a_squared = a ** 2
    # For each number b between 1 and 1000...
    for b in range(1, 1000):
        # Find b squared
        b_squared = b ** 2
        # Find the square root of a squared and b squared, which is c
        c = math.sqrt(a_squared + b_squared)

        # If c is an integer, and the sum of a, b and c is 1000....
        if c.is_integer() and a + b + c == 1000:
            # Multiply the three together
            pythagorean_triplet_product = a * b * int(c)

print(pythagorean_triplet_product)
