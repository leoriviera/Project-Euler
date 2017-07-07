# Solved correctly
def palindrome_det(possible_palindrome):
        digit_list, digit_reversed = [], []
        digit_list = list(str(possible_palindrome))

        list_length = len(digit_list) - 1
        for digit in range(list_length, -1, -1):
            digit_reversed.append(digit_list[digit])    

        if digit_list == digit_reversed:
            return True
        else:
            return False

total = 0

for n in range(0, 1000000):
    n_palindrome = palindrome_det(n)
    if n_palindrome:
        n_binary = format(n, '0b')
        n_binary_palindrome = palindrome_det(n_binary)
        if n_binary_palindrome:
            total += n

print(total)
