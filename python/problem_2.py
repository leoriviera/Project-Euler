# Solved correctly
sequence = [1, 2]
total = 0

while True:
    sequence_len = len(sequence)
    num_1 = sequence[sequence_len - 1]
    num_2 = sequence[sequence_len - 2]
    
    sequence_next = num_1 + num_2
    if sequence_next < 4000000:
        sequence.append(sequence_next)
    else:
        break

print(sequence)
for num in range(0, len(sequence)):
    is_even = sequence[num] % 2

    if is_even == 0:
        total += sequence[num]

print(total)
