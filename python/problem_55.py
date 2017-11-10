lychrel_count = 0

def palindrome_det(possible_palindrome):
    digit_reversed = [], []
    digit_list = list(str(possible_palindrome))

    digit_reversed = list(digit for digit in reversed(digit_list))

    if digit_list == digit_reversed and n != possible_palindrome:
        return True
    else:
        digit_reversed = int(''.join(digit_reversed))
        return digit_reversed

for n in range(1, 10000):
    palindrome_1 = n

    for iteration in range(0, 50 + 1):
        is_palindrome = palindrome_det(palindrome_1)

        if is_palindrome != True:
            palindrome_2 = is_palindrome
            palindrome_1 += palindrome_2
        elif is_palindrome and palindrome_1 != n:
            break

    if is_palindrome != True:
        lychrel_count += 1

print(lychrel_count)
