# Solved correctly
products, palindrome_products = [], []
answer = 0

for factor_1 in range(100, 1000):
    for factor_2 in range(100, 1000):
        product = factor_1 * factor_2
        products.append(product)

products = list(set(products))

for palindrome_index in range(0, len(products)):
    possible_palindrome = products[palindrome_index]
    digit_list, digit_reversed = [], []
    digit_list = list(str(possible_palindrome))

    list_length = len(digit_list) - 1
    for digit in range(list_length, -1, -1):
        digit_reversed.append(digit_list[digit])    

    if digit_list == digit_reversed:
        palindrome_products.append(possible_palindrome)

palindrome_products.sort()
answer = palindrome_products[len(palindrome_products) - 1]
print(answer)
