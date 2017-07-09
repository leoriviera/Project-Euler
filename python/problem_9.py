# Solved correctly
import math as maths

pythagorean_triplet = []

for a in range(1, 1000):
    a_squared = a ** 2
    for b in range(1, 1000):
        b_squared = b ** 2
        c = maths.sqrt(a_squared + b_squared)
        c_integer = c.is_integer()

        if c_integer and a + b + c == 1000:
            pythagorean_triplet.append(a)
            pythagorean_triplet.append(b)
            pythagorean_triplet.append(int(c))

        if len(pythagorean_triplet) == 3:
            break

    if len(pythagorean_triplet) == 3:
        pythagorean_triplet_product = pythagorean_triplet[0] * \
            pythagorean_triplet[1] * pythagorean_triplet[2]
        break

print(pythagorean_triplet_product)
