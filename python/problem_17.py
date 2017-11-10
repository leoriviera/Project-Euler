ones = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
tens = {'1': 3, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
teens = {'1': 6, '2': 6, '3': 8, '4': 8, '5': 7, '6': 7, '7': 9, '8': 8, '9': 8}
places = {'h': 7, 'a': 3}

total = 0

def wordToNumber(string_n):
    hundreds_place = string_n[0]
    tens_place = string_n[1]
    ones_place = string_n[2]

    if tens_place == '':
        tens_place = 0

    if hundreds_place == '':
        hundreds_place = 0

    number_length = 0

    if tens_place != '0' and tens_place != '1' and ones_place != '0':
        number_length += tens[tens_place] + ones[ones_place]
    elif tens_place == '1' and ones_place != '0':
        number_length += teens[ones_place]
    elif tens_place != '0' and ones_place == '0':
        number_length += tens[tens_place]
    elif tens_place == '0' and ones_place != '0':
        number_length += ones[ones_place]

    if hundreds_place != '0':
        number_length += ones[hundreds_place] + places['h']

    if hundreds_place != '0' and (tens_place != '0' or ones_place != '0'):
        number_length += places['a']

    print(three_digit_string, number_length)

    return number_length

for n in range(1, 1000):
    string = str(n)
    if len(string) == 3:
        three_digit_string = string[0] + string[1] + string[2]
    elif len(string) == 2:
        three_digit_string = '0' + string[0] + string[1]
    elif len(string) == 1:
        three_digit_string = '0' + '0' + string[0]

    total += wordToNumber(three_digit_string)
total += len('onethousand')

print(total)
