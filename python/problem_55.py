def problem_55():
    "How many Lychrel numbers are there below ten-thousand?"

    lychrel_count = 0

    def is_palindrome(integer):
        # Convert the integer to a string
        string = str(integer)
        # Reverse the string and join it back together
        reversed_string = ''.join(reversed(string))
        # If two strings are equal...
        if(string == reversed_string):
            # Return true
            return True
        # Otherwise, return the reversed number
        return int(reversed_string)

    # For fifty iterations of each number below 10000...
    for n in range(1, 10000):
        for iteration in range(0, 50 + 1):
            # Check whether the number is a palindrome
            palindrome = is_palindrome(n)
            # If it is, break the loop.
            if(palindrome == True):
                break
            # Otherwise, add the reversed number to n
            n += palindrome

        # If, after the iterations, the number is not a palindrome...
        if(palindrome is not True):
            # Add one to the lychrel count
            lychrel_count += 1

    return lychrel_count


if __name__ == "__main__":
    answer = problem_55()
    print(answer)
