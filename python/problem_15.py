grid_size = 20
lattice_path_corners = []

for y_1 in range(0, grid_size + 1):
    path_row = []
    for x_1 in range(0, grid_size + 1):
        if x_1 == 0 or y_1 == 0:
            path_row.append(1)
        else:
            path_row.append(0)
    lattice_path_corners.append(path_row)

for y_2 in range(1, grid_size + 1):
    for x_2 in range(1, grid_size + 1):
        one_up = lattice_path_corners[x_2][y_2 - 1]
        one_down = lattice_path_corners[x_2 - 1][y_2]
        lattice_path_corners[x_2][y_2] = one_up + one_down

print(lattice_path_corners[grid_size][grid_size])
