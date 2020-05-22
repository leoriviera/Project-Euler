def problem_25():
    "What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"

    # Start the sequence off with 1 and 1.
    sequence = [1, 1]
    latest_sequence_string = ''

    # While the last entry in the sequence is smaller than 10^999 (a number with 1000 digits)...
    while sequence[-1] < (10 ** (1000 - 1)):
        # Add the two previous entries in the sequence to make next entry
        next_in_sequence = sequence[-1] + sequence[-2]
        # Append next entry to sequence
        sequence.append(next_in_sequence)

    # Find the length of the sequence
    index = len(sequence)

    return index


if __name__ == "__main__":
    answer = problem_25()
    print(answer)
