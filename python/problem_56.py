def problem_56():
    "Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?"

    maximum_digital_sum = 0

    for a in range(1, 100):
        for b in range(1, 100):
            result = str(a**b)
            digital_sum = sum([int(digit) for digit in result])

            if digital_sum > maximum_digital_sum:
                maximum_digital_sum = digital_sum

    return maximum_digital_sum


if __name__ == "__main__":
    answer = problem_56()
    print(answer)
