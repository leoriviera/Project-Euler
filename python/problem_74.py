import math as maths

chain_count = 0

for n in range(1, 1000000):
    terms = [n]
    chain_link = n
    factorial_sum = 0

    while factorial_sum not in terms:
        string = str(chain_link)

        for digit_index in range(0, len(string)):
            digit = int(string[digit_index])
            factorial_sum += maths.factorial(digit)

        if factorial_sum not in terms:
            terms.append(factorial_sum)
            chain_link = factorial_sum
            factorial_sum = 0

    if len(terms) == 60:
        chain_count += 1

print(chain_count)