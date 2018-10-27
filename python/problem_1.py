# Solved correctly
total = 0

# For each number, num, between 1 and 1000...
for num in range(1, 1000):
    # Find the modulus of 3 and the modulus of 5.
    mod_3 = (num % 3)
    mod_5 = (num % 5)

    # If both the remainders equal 0...
    if(mod_3 == 0 or mod_5 == 0):
        # Add the number to the total.
        total += num

print(total)
