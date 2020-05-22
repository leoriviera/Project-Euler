import math


def problem_39():
    "If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, for which value of p ≤ 1000, is the number of solutions maximised?"

    each_solutions_count = []

    for p in range(1, 1000 + 1):
        p_solutions_count = 0
        for a in range(1, p):
            for b in range(1, a):
                c = math.sqrt((a ** 2) + (b ** 2))
                if c.is_integer() and a + b + c == p:
                    p_solutions_count += 1
        each_solutions_count.append(p_solutions_count)

    max_solutions_count = each_solutions_count.index(max(
        solutions_count for solutions_count in each_solutions_count)) + 1

    return max_solutions_count


if __name__ == "__main__":
    answer = problem_39()
    print(answer)
