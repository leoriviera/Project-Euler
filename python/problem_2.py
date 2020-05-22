def problem_2():
    "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
    sequence = [1]
    total, sequence_next = 0, 0

    # While the next term in the Fibonacci sequence is under 4000000...
    while(sequence_next < 4000000):
        # Calculate the next term in the sequence and append it to the list
        sequence_next = sequence[len(sequence) - 1] + \
            sequence[len(sequence) - 2]
        sequence.append(sequence_next)

        # If the entry is even, add it to the sum of even numbered terms
        if(sequence_next % 2 == 0):
            total += sequence_next

    return total


if __name__ == "__main__":
    answer = problem_2()
    print(answer)
