# Solved correctly
max_a, max_b = 0, 0
max_consecutive_prime = 0


def is_prime(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
        elif divisor == num - 1:
            return True


for a in range(-1000, 1000 + 1):
    for b in range(-999, 1000):
        n = 0
        while True:
            n_squared = n ** 2
            quadratic_result = n_squared + (a * n) + b
            if is_prime(quadratic_result):
                n += 1
            elif n > max_consecutive_prime:
                max_consecutive_prime = n
                max_a, max_b = a, b
                break
            else:
                break

print(max_a * max_b)
