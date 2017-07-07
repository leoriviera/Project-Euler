# Solved correctly
num = 2

while True:
    total = 0
    for div in range(2, 21):
        if num % div != 0:
            num += 1
            break
        else:
            total += 1
    if total == 19:
        break

print(num)
