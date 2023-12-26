from math import sqrt
from itertools import combinations
from statistics import median


def calculate_distance(pair):
    (a, b) = pair
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def minimum_distance(points):
    if len(points) <= 3:
        return min([calculate_distance(pair) for pair in combinations(points, 2)])

    c = median([p[0] for p in points])

    left = []
    right = []

    for p in points:
        if p[0] < c:
            left.append(p)
        else:
            right.append(p)

    delta = min(minimum_distance(left), minimum_distance(right))

    b_left = filter(lambda p: abs(p[0] - c) < delta, left)
    b_right = sorted(filter(lambda p: abs(p[0] - c) < delta, right), key=lambda p: p[1])

    minimum = delta

    for point_l in b_left:
        for point_r in b_right:
            l_r_distance = calculate_distance((point_l, point_r))
            if l_r_distance < minimum:
                minimum = l_r_distance

    return minimum


def d(k):
    max_n = 2 * k

    s = [290797]

    for n in range(1, max_n):
        s.append((s[n - 1] ** 2) % 50515093)

    p = [(s[2 * n], s[(2 * n) + 1]) for n in range(k)]

    minimum = minimum_distance(p)

    return minimum


def problem_816():
    return round(d(2_000_000), 9)


if __name__ == "__main__":
    answer = problem_816()
    print(answer)
