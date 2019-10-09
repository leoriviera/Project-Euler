# Solved correctly
# Calculate the value of the non-Mersenne prime and convert to string
non_mersenne_prime = str(28433 * 2 ** 7830457 + 1)
# Extract substring of last ten digits
final_digits = non_mersenne_prime[-10:]

print(final_digits)
