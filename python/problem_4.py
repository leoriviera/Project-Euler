# Solved correctly
products, palindrome_products = [], []

for factor_1 in range(100, 1000):
    for factor_2 in range(100, 1000):
        products.append(factor_1 * factor_2)

products = list(set(products))

for palindrome_index in range(0, len(products)):
    possible_palindrome = products[palindrome_index]
    digit_list = list(str(possible_palindrome))

    digit_reversed = [digit for digit in reversed(digit_list)]

    if digit_list == digit_reversed:
        palindrome_products.append(possible_palindrome)

print(palindrome_products[len(palindrome_products) - 1])
