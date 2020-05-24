from snippets import list_proper_divisors


def problem_21():
    amicable_list = []

    for a in range(2, 10000 + 1):
        if (a in amicable_list):
            continue

        b = sum(list_proper_divisors(a))

        if (a == b):
            continue

        if (a == sum(list_proper_divisors(b))):
            amicable_list.extend([a, b])

    amicable_sum = sum(amicable_list)

    return amicable_sum


if __name__ == "__main__":
    answer = problem_21()
    print(answer)
