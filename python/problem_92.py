# Solved successfully
def find_chain(i):
    # Find square digit chains, starting from a number i
    global one_chain, two_chain

    # Create list to store current chain
    current_chain = []
    n = i

    # While loop has not been discontinued
    while True:
        # Add n to the chain
        current_chain.append(n)
        # Convert n into a string
        n_str = list(str(n))

        # Initialise t, square digit total
        t = 0

        # Iterate through n, squaring and adding digits
        for digit in n_str:
            t += int(digit) ** 2

        # If square digit total is 1, or in the first set of results...
        if (t == 1) or (t in one_chain):
            # Add the current chain to the list of chains
            one_chain.update(current_chain)
            # Reset the current chain
            current_chain = []
            # Return false
            return False
        # Otherwise, if square digit total is 89, or in the second list...
        elif (t == 89) or (t in two_chain):
            # Update list of chains with current chain
            two_chain.update(current_chain)
            # Reset current chain
            current_chain = []
            # Return true
            return True

        # Set n to square digit total
        n = t


# Create sets to store chains
one_chain = set([1])
two_chain = set([89])

count = 0
power = 7


# For each number between 2 and 10^7
for i in range(2, 10 ** power):
    # Find the chain end
    chain_end = find_chain(i)
    # If the chain ends at 89...
    if chain_end:
        # Add one to the count
        count += 1
