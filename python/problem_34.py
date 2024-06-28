import math


def problem_34():
    def sum_digit_factorial(n):
        return sum([math.factorial(int(digit)) for digit in str(n)])

    total = 0

    for i in range(3, 150000):
        if i == sum_digit_factorial(i):
            total += i

    return total


if __name__ == "__main__":
    answer = problem_34()
    print(answer)
