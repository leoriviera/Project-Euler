# Solved correctly
self_powers_total = 0
last_ten_digits = ''

for n in range(1, 1000 + 1):
    self_powers_total += n ** n

self_powers_total = str(self_powers_total)
self_powers_length = len(self_powers_total)

for digit_index in range(self_powers_length - 10, self_powers_length):
    digit = self_powers_total[digit_index]
    last_ten_digits += digit

print(last_ten_digits)
