# Solved correctly
sum_square, square_sum = 0, 0
total = 0

for num in range(1, 100 + 1):
    total += num
    sum_square += num ** 2

square_sum = total * total

print(square_sum - sum_square)
