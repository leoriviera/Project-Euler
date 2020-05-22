def problem_5():
    "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

    # Start the number from 2520
    num = 2520

    while True:
        # Set a flag to False
        flag = False
        # For each divisor between 11 and 20...
        for div in range(11, 20 + 1):
            # If a number is not divisible by a divisor...
            if(num % div != 0):
                # Increase the number by 10 and set the flag to True
                num += 10
                flag = True
                break
        # If the flag hasn't been triggered, break the loop
        if(not flag):
            break

    return num


if __name__ == "__main__":
    answer = problem_5()
    print(answer)
