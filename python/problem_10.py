# Solved correctly
primes = [2]
answer, n, target = 0, 3, 2000000

while True:
    for divisor in range(2, n):
        if n % divisor == 0:
            n += 1
            break
        elif divisor == n - 1 and n < target:
            primes.append(n)
            print(len(primes), n)
            n += 1

    if n > target:
        break

for prime_index in range(0, len(primes)):
    answer += primes[prime_index] 

print(answer)
