def problem_45():
    "Find the next triangle number [after 40755] that is also pentagonal and hexagonal."

    def triangleNGenerator(n):
        t_n = n * (n + 1) / 2
        return t_n

    def pentagonNGenerator(n):
        p_n = n * (3 * n - 1) / 2
        return p_n

    def hexagonNGenerator(n):
        h_n = n * (2 * n - 1)
        return h_n

    triangle_n_list = []
    pentagon_n_list = []
    hexagon_n_list = []

    while True:
        triangle_n = triangleNGenerator(count)
        pentagon_n = pentagonNGenerator(count)
        hexagon_n = hexagonNGenerator(count)

        triangle_n_list.append(triangle_n)
        pentagon_n_list.append(pentagon_n)
        hexagon_n_list.append(hexagon_n)

        if triangle_n in pentagon_n_list and triangle_n in hexagon_n_list:
            if triangle_n != 1 and triangle_n != 40755:
                return triangle_n


if __name__ == "__main__":
    answer = problem_45()
    print(answer)
