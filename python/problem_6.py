# Solved correctly
sum_square, square_sum = 0, 0
total = 0

# For each number between 1 and 100...
for num in range(1, 100 + 1):
    # Add the number to the total...
    total += num
    # Square the number and add it to the sum of squares...
    sum_square += num ** 2

# Square the total and calculate difference
square_sum = total * total
difference = square_sum - sum_square

print(difference)
