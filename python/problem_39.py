import math

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
print(max_solutions_count)
