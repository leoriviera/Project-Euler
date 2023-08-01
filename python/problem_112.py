
def problem_112():
    total = 21780
    bouncy_count = 19602

    def is_bouncy(n):
        diff = []

        for i in range(1, len(str(n))):
            current_digit = int(str(n)[i])
            preceding_digit = int(str(n)[i - 1])

            if current_digit > preceding_digit:
                diff.append(1)

            if current_digit < preceding_digit:
                diff.append(-1)

            if current_digit == preceding_digit:
                diff.append(0)

        unique = set(diff)

        return 1 in unique and -1 in unique

    n = 21780

    while (bouncy_count / n) != 0.99:
        n += 1

        if(is_bouncy(n)):
            bouncy_count += 1

        total += 1

    return n


if __name__ == "__main__":
    answer = problem_112()
    print(answer)
