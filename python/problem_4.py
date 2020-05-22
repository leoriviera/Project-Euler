from snippets import is_palindrome


def problem_4():
    "Find the largest palindrome made from the product of two 3-digit numbers."

    largest_product = 0
    # With one factor between 100 and 1000...
    for factor_one in range(100, 999 + 1):
        # And with a second factor between 100 and 1000...
        for factor_two in range(factor_one, 999 + 1):
            # Calculate the product of the two factors
            product = factor_one * factor_two
            # If the product is a palindrome and is larger than the largest product...
            if(is_palindrome(product) and product > largest_product):
                # Set the largest product to the current product
                largest_product = product

    return largest_product


if __name__ == "__main__":
    answer = problem_4()
    print(answer)
