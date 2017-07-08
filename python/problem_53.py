# Solved correctly
import math as maths

total = 0

for n in range(1, 100 + 1):
    print(n)
    for r in range(1, n + 1):
        n_factorial = maths.factorial(n)
        r_factorial = maths.factorial(r)
        n_minus_r_factorial = maths.factorial(n - r)

        n_C_r = n_factorial / (r_factorial * n_minus_r_factorial)
        if n_C_r > 1000000:
            total += 1

print(total)
