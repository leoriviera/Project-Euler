
def problem_31():
    "How many different ways can £2 be made using any number of 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p) coins?"

    # Get the target value of the coin, as well as all possible coin values (in pence)
    target_value = 200
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

    polynomials_list = []

    # For all coin values...
    for value in coin_values:
        # Generate a polynomial representing all values which can be made solely
        # by this coin, up to and including the target value
        polynomials_list.append(
            {k: 1 for k in range(0, target_value + 1, value)})

    # Start with a polynomial, f, popped off the generated list
    f = polynomials_list.pop()

    # For each remaining polynomial expression...
    for expression in polynomials_list:
        polynomial_product = {}

        # For each exponent in the expression...
        for k in expression.keys():
            # And for each exponent in f...
            for j in f.keys():
                # Add the powers
                power = k + j
                # Multiply the coefficients
                coefficient = (expression[k] * f[j])

                # If the power doesn't exist in the multiplied polynomial...
                if(power not in polynomial_product.keys()):
                    # Set that exponent's product to 0
                    polynomial_product[power] = 0

                # Add the calculated coefficient to the coefficient on the product
                polynomial_product[power] += coefficient

        # Set f to the polynomial product
        f = polynomial_product

    # Return the coefficient of x^200, which is how many ways 200p can be formed from the specified coin_values
    return f[200]


if __name__ == "__main__":
    answer = problem_31()
    print(answer)
