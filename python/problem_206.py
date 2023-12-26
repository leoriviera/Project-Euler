from math import ceil, floor, sqrt


def problem_206():
    start = floor(sqrt(1_020_304_050_607_080_900))
    end = ceil(sqrt(1_929_394_959_697_989_999))

    for n in range(start, end + 1, 10):
        s = str(n**2)

        digits = "".join([s[i] for i in range(0, 19, 2)])

        if digits == "1234567890":
            return n


if __name__ == "__main__":
    answer = problem_206()
    print(answer)
