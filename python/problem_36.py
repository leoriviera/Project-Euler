# Solved correctly
from snippets import is_palindrome


def problem_36():
    "Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."

    total = 0

    # For each integer, n, between 1 and 1000000...
    for n in range(1, 1000000):
        # If number is a palindrome...
        if is_palindrome(n):
            # Convert number to binary
            n_binary = format(n, '0b')
            # If n in binary is a palindrome...
            if is_palindrome(n_binary):
                # Add n to the total
                total += n

    return total


if __name__ == "__main__":
    answer = problem_36()
    print(answer)
