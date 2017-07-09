# Solved correctly
non_mersenne_prime = 28433 * 2 ** 7830457 + 1
non_mersenne_prime_string = str(non_mersenne_prime)

last_ten_digits = ''

for digit_index in range(
        len(non_mersenne_prime_string) - 10,
        len(non_mersenne_prime_string)):
    last_ten_digits += non_mersenne_prime_string[digit_index]

print(last_ten_digits)
