total = 0

for n in range(2, 500000):
    digit_sum = 0
    string = str(n)

    for digit_index in range(0, len(string)):
        digit = int(string[digit_index])
        digit_sum += pow(digit, 5)

    if digit_sum == n:
        total += n

    print(total)