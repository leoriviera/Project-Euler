# Solved correctly
indices, product = [1, 10, 100, 1000, 10000, 100000, 1000000], 1

constant = ''.join(str(digit) for digit in range(1, 1000000 + 1))

for index in indices:
    product *= int(constant[index - 1])

print(product)
