# Solved correctly
sum_square, square_sum = 0, 0
total, answer = 0, 0 

for num in range(1, 101):
    total += num
    sum_square += num ** 2

square_sum = total * total

answer = square_sum - sum_square
print(answer)
