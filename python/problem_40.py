def problem_40():
    "An irrational decimal fraction is created by concatenating the positive integers. If d_n represents the nth digit of the fractional part, find the value of the following expression. d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000."

    indices, product = [1, 10, 100, 1000, 10000, 100000, 1000000], 1

    constant = ''.join(str(digit) for digit in range(1, 1000000 + 1))

    for index in indices:
        product *= int(constant[index - 1])

    return product


if __name__ == "__main__":
    answer = problem_40()
    print(answer)
