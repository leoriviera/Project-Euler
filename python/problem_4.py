# Solved correctly
def int_palindrome_check(integer):
    # Convert the integer to a string
    string = str(integer)
    # Reverse the string and join it back together
    reversed_string = ''.join(reversed(string))
    # If two strings are equal...
    if(string == reversed_string):
        # Return true
        return True
    return False

largest_product = 0
# With one factor between 100 and 1000...
for factor_one in range(100, 999 + 1):
    # And with a second factor between 100 and 1000...
    for factor_two in range(factor_one, 999 + 1):
        # Calculate the product of the two factors
        product = factor_one * factor_two
        # If the product is a palindrome and is larger than the largest product...
        if(int_palindrome_check(product) and product > largest_product):
            # Set the largest product to the current product
            largest_product = product

print(largest_product)
