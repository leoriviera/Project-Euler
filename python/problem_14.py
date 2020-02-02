# Solved correctly
longest_length = 0
longest_start = 0

# For each number between 1 and one million...
for i in range(1, 1000000):
    # Take a copy of each number
    n = i
    # Set the length of the chain to 1
    length = 1
    # While n is not 1...
    while n != 1:
        # If the number is even...
        if n % 2 == 0:
            # Floor divide the number by 2
            n /= 2
            # Increase the length of the chain by 1
            length += 1
        # Otherwise, if the number is odd...
        else:
            n = ((3 * n) + 1)
            length += 1
    if(length > longest_length):
        longest_length = length
        longest_start = i


print(longest_start)
