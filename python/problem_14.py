# Solved correctly
chain_length_unsorted, chain_length_sorted = [], []

for i in range(1, 1000000):
    n = i
    length = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            length += 1
        else:
            n *= 3
            n += 1
            length += 1
    chain_length_sorted.append(length)
    chain_length_unsorted.append(length)

chain_length_sorted.sort()
highest_collatz_chain = chain_length_sorted[len(chain_length_sorted) - 1]
starting_n = chain_length_unsorted.index(highest_collatz_chain) + 1

print(starting_n)
