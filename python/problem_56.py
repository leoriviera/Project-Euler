# Solved correctly
maximum_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        power = str(a ** b)
        digital_sum = sum(int(power[index]) for index in range(0, len(power)))

        if digital_sum > maximum_digital_sum:
            maximum_digital_sum = digital_sum

print(maximum_digital_sum)
