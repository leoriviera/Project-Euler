# Solved correctly
sequence = [1, 1]
latest_sequence_string = ''

while len(latest_sequence_string) < 1000:
    latest_sequence_index = len(sequence) - 1
    latest_sequence_string = str(sequence[latest_sequence_index])

    next_in_sequence = sequence[latest_sequence_index] + \
        sequence[latest_sequence_index - 1]
    sequence.append(next_in_sequence)

answer = len(sequence) - 1

print(answer)
