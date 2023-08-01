def problem_48():
    "Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000"

    total = 0
    # For each number n between 1 and 1000...
    for n in range(1, 1000 + 1):
        total += n ** n

    # Convert the total to a string
    total = str(total)
    # Extract the final ten digits
    final_digits = total[-10:]

    return int(final_digits)


if __name__ == "__main__":
    answer = problem_48()
    print(answer)
