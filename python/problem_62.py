def problem_62():
    "Find the smallest cube for which exactly five permutations of its digits are cube."

    TARGET = 5
    permutations = {}
    i = 0

    # While the permutations dictionary is empty or the maximum number of
    # cubic permutations does not equal the target
    while permutations == {} or max([len(p) for p in permutations.values()]) != TARGET:
        i += 1
        cube = i**3
        digits = "".join(sorted(str(cube)))

        if digits not in permutations:
            permutations[digits] = []

        permutations[digits].append(cube)

    # Get item with most permutations
    values = max(permutations.items(), key=lambda p: len(p[1]))

    return values[1][0]


if __name__ == "__main__":
    answer = problem_62()
    print(answer)
