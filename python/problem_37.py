from snippets import is_prime


def problem_37():
    primes = [2, 3, 5, 7]

    t_primes = []

    n = 10

    def truncate_left(str_n):
        t = [int(str_n[0:i]) for i in range(1, len(str_n))]

        return t

    def truncate_right(str_n):
        l = len(str_n)
        t = [int(str_n[i:l]) for i in range(1, len(str_n))]

        return t

    while len(t_primes) < 11:
        n += 1

        # print(n)
        if not is_prime(n):
            continue

        primes.append(n)

        str_n = str(n)

        t_l_prime = map(is_prime, truncate_left(str_n))
        t_r_prime = map(is_prime, truncate_right(str_n))

        if all(t_l_prime) and all(t_r_prime):
            t_primes.append(n)

    return sum(t_primes)


if __name__ == "__main__":
    answer = problem_37()
    print(answer)
