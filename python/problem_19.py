# Solved correctly
# Calculate the length of the month using the day and the year
def month_length_calc(m, y):
    # If the month is February...
    if m == 2:
        # If the year is divisible by four, and the year is not divisible by 100...
        if y % 4 == 0 and y % 100 != 0:
            # Return 29
            return 29
        # If the year is divisible by 100 and by 400...
        elif y % 100 == 0 and y % 400 == 0:
            # Return 29
            return 29
        else:
            # Otherwise, return 28
            return 28

    # If the month is April, June, October or November...
    if month == 4 or month == 6 or month == 9 or month == 11:
        # Return 30
        return 30
    else:
        # Otherwise, return 31
        return 31


sunday_count, year_day = 0, 1
# For each month in year between 1900 and 2000...
for year in range(1900, 2000 + 1):
    for month in range(1, 12 + 1):
        # Calculate the length of the month
        month_length = month_length_calc(month, year)
        # For each day in the month...
        for each_day in range(1, month_length + 1):
            # Add one to the number of total days...
            year_day += 1
            # If the total number of days is divisible by seven,
            # the day falls on the first of the month,
            # and the year is not 1900...
            if year_day % 7 == 0 and each_day == 1 and year > 1900:
                # Add one to the number of Sundays
                sunday_count += 1

print(sunday_count)
