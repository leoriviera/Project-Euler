def problem_30():
    "Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."

    total = 0

    # For each number between 2 and 500000, exclusive...
    for n in range(2, 500000):
        string = str(n)
        # Find the sum of the digit^5, for each digit in the number
        digit_sum = sum(pow(int(digit), 5) for digit in string)

        # If the sum of the digit fifth powers is n...
        if digit_sum == n:
            # Add n to the total
            total += n

    return total


if __name__ == "__main__":
    answer = problem_30()
    print(answer)
