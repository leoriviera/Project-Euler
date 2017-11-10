# Solved correctly
integer_combinations = set()

for a in range(2, 100 + 1):
    for b in range(2, 100 + 1):
        power = a ** b
        integer_combinations.add(power)

print(len(integer_combinations))
