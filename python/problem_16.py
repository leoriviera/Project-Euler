def problem_16():
    "What is the sum of the digits of the number 2^1000?"

    # Calculate 2^1000 and convert it to a string
    two_to_thousand, total = str(2 ** 1000)

    # Add each of the digits to find the total
    total = sum([int(digit) for digit in two_to_thousand])

    return total


if __name__ == "__main__":
    answer = problem_16()
    print(answer)
