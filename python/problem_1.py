# Solved correctly
total = 0

for num in range(1, 1000):
    mod_3 = num % 3
    mod_5 = num % 5

    if mod_3 == 0 or mod_5 == 0:
        total += num

print(total)
