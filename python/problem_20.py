import math


def problem_20():
    "Find the sum of the digits in the number 100!"

    # Calculate 100! and convert to a string
    factorial = str(math.factorial(100))

    # Calculate the sum of the digits in the string
    total = sum([int(digit) for digit in factorial])

    return total


if __name__ == "__main__":
    answer = problem_20()
    print(answer)
