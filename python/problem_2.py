# Solved correctly
sequence = [1]
total = 0

while True:
    sequence_next = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]

    if sequence_next < 4000000:
        sequence.append(sequence_next)
    else:
        break

    if sequence_next % 2 == 0:
           total += sequence_next 

print(total)
