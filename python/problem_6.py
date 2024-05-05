def problem_6():
    "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."

    sum_of_square = sum(map(lambda n: n**2, range(1, 100 + 1)))
    square_of_sum = sum(range(1, 100 + 1)) ** 2

    difference = square_of_sum - sum_of_square

    return difference


if __name__ == "__main__":
    answer = problem_6()
    print(answer)
