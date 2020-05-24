from snippets import simplify_fraction


def problem_33():
    "In the first one-thousand expansions [of the square root of 2], how many fractions contain a numerator with more digits than the denominator?"

    def can_cancel_simplify_fraction(fraction):
        "Can a fraction be simplified by cancelling digits?"

        # Get digits in numerator and denominator
        numerator = list(str(fraction[0]))
        denominator = list(str(fraction[1]))

        # Get unique digits in numerator and denominator
        numerator_set = set(numerator)
        denominator_set = set(denominator)

        # Get the similar digits
        similar_digit = numerator_set.intersection(denominator_set)

        # If there is a similar digit,
        # and the numerator and denominator are not the same
        if (len(similar_digit) == 1 and numerator != denominator):
            # Pop the digit
            digit = similar_digit.pop()

            # If the digit is greater than zero,
            # and therefore the case is not trivial
            if (int(digit) > 0):
                # Cancel the digit from the
                # numerator and denominator
                numerator.remove(digit)
                denominator.remove(digit)

                # Convert the remaining digit in the
                # numerator and denominator to integers
                numerator = int(numerator[0])
                denominator = int(denominator[0])

                # If the denominator is non-zero
                if (denominator > 0):
                    cancelled_fraction = (numerator, denominator)

                    # Simplify the fraction and the cancelled fraction
                    simplified_fraction = simplify_fraction(fraction)
                    simplified_cancelled = simplify_fraction(
                        cancelled_fraction)

                    # Find the value of the fraction
                    # and the cancelled fraction
                    fraction_value = simplified_fraction[0] / \
                        simplified_fraction[1]
                    cancelled_value = simplified_cancelled[0] / \
                        simplified_cancelled[1]

                    # If the values are equal...
                    if (fraction_value == cancelled_value):
                        # The fraction can be simplified by
                        # cancelling digits in numerator and
                        # denominator
                        return True

        # Return false
        return False

    fractions = []

    for denominator in range(10, 99 + 1):
        for numerator in range(10, denominator + 1):
            # If cancelling digits can simplify the fraction...
            if (can_cancel_simplify_fraction((numerator, denominator))):
                # Append the fraction to the list
                fractions.append((numerator, denominator))

    numerator = 1
    denominator = 1

    # For each fraction...
    for fraction in fractions:
        # Multiply the numerator and denominator
        numerator *= fraction[0]
        denominator *= fraction[1]

    # Simplify the fraction
    simplified_product = simplify_fraction((numerator, denominator))

    # Return the denominator
    return simplified_product[1]


if __name__ == "__main__":
    answer = problem_33()
    print(answer)
