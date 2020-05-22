def problem_28():
    "What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral [starting with the number 1 and moving to the right in a clockwise direction]?"

    row = 1001
    # Calculates number of diagonals in a spiral with row rows
    diagonal_count = ((row - 1) * 2)
    diagonals = [1]

    # Set the number added to the diagonals
    diagonal_add = 2

    # For each number between 1 and the number of diagonals, inclusive
    for i in range(1, diagonal_count + 1):
        # Increase the previous diagonal by diagonal_add and append to list
        diagonals.append(diagonals[i - 1] + diagonal_add)
        # The number of the diagonals increases by 2 every four numbers, because each spiral has four diagonals.
        # Thus, if i is a multiple of four, add 2 to diagonal_add
        if(i % 4 == 0):
            diagonal_add += 2

    diagonals_sum = sum(diagonals)

    return diagonals_sum


if __name__ == "__main__":
    answer = problem_28()
    print(answer)
