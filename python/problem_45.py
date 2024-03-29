def problem_45():
    "Find the next triangle number [after 40755] that is also pentagonal and hexagonal."

    def triangle_n_generator(n):
        t_n = n * (n + 1) / 2
        return t_n

    def pentagon_n_generator(n):
        p_n = n * (3 * n - 1) / 2
        return p_n

    def hexagon_n_generator(n):
        h_n = n * (2 * n - 1)
        return h_n

    count = 1

    triangle_n_list = []
    pentagon_n_list = []
    hexagon_n_list = []

    while True:
        triangle_n = triangle_n_generator(count)
        pentagon_n = pentagon_n_generator(count)
        hexagon_n = hexagon_n_generator(count)

        triangle_n_list.append(triangle_n)
        pentagon_n_list.append(pentagon_n)
        hexagon_n_list.append(hexagon_n)

        if triangle_n in pentagon_n_list and triangle_n in hexagon_n_list:
            if triangle_n != 1 and triangle_n != 40755:
                return triangle_n

        count += 1


if __name__ == "__main__":
    answer = problem_45()
    print(answer)
