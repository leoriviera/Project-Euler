# Solved correctly
primes = []
n, target = 3, 10001

while len(primes) < target - 1:
    for divisor in range(2, n):
        if n % divisor == 0:
            n += 1
            break
        elif divisor == n - 1:
            primes.append(n)
            n += 1

prime_index = len(primes) - 1
print(primes[prime_index])