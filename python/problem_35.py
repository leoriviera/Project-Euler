# Solved correctly
from snippets import is_prime


def problem_35():
    "How many circular primes are there below one million, where [all rotations of the digits are themselves prime]?"

    def is_cycle_prime(num):
        for i in range(0, len(str(num))):
            if not is_prime(num):
                return False
            num = str(num)
            num = num[len(num) - 1] + num[:-1]
            num = int(num.lstrip("0"))
        return True

    prime_count = 1
    for i in range(3, 1000000, 2):
        if is_cycle_prime(i):
            prime_count = prime_count + 1

    return prime_count


if __name__ == "__main__":
    answer = problem_35()
    print(answer)
