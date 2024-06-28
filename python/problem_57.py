from fractions import Fraction


def problem_57():
    n = 0

    c = Fraction(1, 2)

    for _ in range(1000):
        v = 1 + c

        if len(str(v.numerator)) > len(str(v.denominator)):
            n += 1

        c = Fraction(1, 2 + c)

    return n


if __name__ == "__main__":
    answer = problem_57()
    print(answer)
