# Solved correctly
def month_length_calc(m, y):
    if m == 2:
        if y % 4 == 0 and y % 100 != 0:
            return 29
        elif y % 100 == 0 and y % 400 == 0:
            return 29
        else:
            return 28

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31

sunday_count, month_day = 0, 1 

for year in range(1900, 2000 + 1):
    for month in range(1, 12 + 1):
        month_length = month_length_calc(month, year)
        for each_day in range(1, month_length + 1):
            month_day += 1
            if month_day % 7 == 0 and each_day == 1 and year > 1900:
                sunday_count += 1
    
print(sunday_count)
