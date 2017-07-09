# Solved correctly
sequence = [1]
total, sequence_next = 0, 0

while sequence_next < 4000000:
    sequence_next = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(sequence_next)

    if sequence_next % 2 == 0:
        total += sequence_next

print(total)
