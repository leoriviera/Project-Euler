# Solved correctly
# Initialise dictionaries containing the number of letters each number in place has
ones = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
tens = {'1': 3, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
teens = {'1': 6, '2': 6, '3': 8, '4': 8,
         '5': 7, '6': 7, '7': 9, '8': 8, '9': 8}
places = {'h': 7, 'a': 3}

total = 0


def numberWordLength(string_n):
    # Find the hundreds, tens and ones place of the three digit number
    hundreds_place = string_n[0]
    tens_place = string_n[1]
    ones_place = string_n[2]

    # If the tens, and hundreds places are empty, set those values to zero.
    if tens_place == '':
        tens_place = 0

    if hundreds_place == '':
        hundreds_place = 0

    number_length = 0

    # If the number is not in the tens, and is not ten, and is not a round number (i.e. 90)...
    if tens_place != '0' and tens_place != '1' and ones_place != '0':
        # Add the tens and ones length to the number
        number_length += tens[tens_place] + ones[ones_place]
    # Else, if part of the the number is in the tens, but is not ten...
    elif tens_place == '1' and ones_place != '0':
        # Add the teens number to the number lengths
        number_length += teens[ones_place]
    # If the tens place is not zero, and the ones place is round (i.e. 90)...
    elif tens_place != '0' and ones_place == '0':
        # Add tens to the number length
        number_length += tens[tens_place]
    # If the number has ones...
    elif tens_place == '0' and ones_place != '0':
        # Add their length to the number length
        number_length += ones[ones_place]

    # If the number has a hundreds place...
    if hundreds_place != '0':
        # Add the ones length of the number, as well as the length of 'hundred'
        number_length += ones[hundreds_place] + places['h']

    # If the number has a hundreds place, and a tens place or a ones place...
    if hundreds_place != '0' and (tens_place != '0' or ones_place != '0'):
        # Add 'and' to the length
        number_length += places['a']

    return number_length


# For each number between one and 1000, exclusive
for n in range(1, 1000):
    # Convert the number to a string...
    string = str(n)
    # Pad the number with leading zeroes.
    if len(string) == 3:
        three_digit_string = string[0] + string[1] + string[2]
    elif len(string) == 2:
        three_digit_string = '0' + string[0] + string[1]
    elif len(string) == 1:
        three_digit_string = '0' + '0' + string[0]

    total += numberWordLength(three_digit_string)

# Manually add the length of 'onethousand'
total += len('onethousand')

print(total)
