# Solved correctly
multiples_3, multiples_5 = [], []
total = 0

for num in range(1, 1000):
    mod_3 = num % 3
    mod_5 = num % 5

    if mod_3 == 0:
        multiples_3.append(num)
    elif mod_5 == 0:
        multiples_5.append(num)
        
for mul_3 in range(0, len(multiples_3)):
    total += multiples_3[mul_3]

for mul_5 in range(0, len(multiples_5)):
    total += multiples_5[mul_5]

print(total)
