def problem_1():
    "Find the sum of all the multiples of 3 or 5 below 1000."

    return sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(1, 1000)))


if __name__ == "__main__":
    answer = problem_1()
    print(answer)
