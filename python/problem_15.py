def problem_15():
    "How many routes are there through a 20×20 grid, [moving right and down from the top left to the top right]?"

    # Set the grid size to 20
    grid_size = 20
    lattice_path_corners = []

    # For each y coordinate in the grid...
    for y_1 in range(0, grid_size + 1):
        path_row = []
        # For each x coordinate in the grid...
        for x_1 in range(0, grid_size + 1):
            # If either coordinate is at the edge, append 1 to the path row.
            if(x_1 == 0 or y_1 == 0):
                path_row.append(1)
            else:
                # Otherwise, append zero.
                path_row.append(0)
        # Append the path row into the lattice path corners
        lattice_path_corners.append(path_row)

    # For each row in the grid, except the first...
    for y_2 in range(1, grid_size + 1):
        # For each column in the grid, except the first...
        for x_2 in range(1, grid_size + 1):
            # Find how many moved available above and below...
            one_up = lattice_path_corners[x_2][y_2 - 1]
            one_down = lattice_path_corners[x_2 - 1][y_2]
            # Append the number of movements to the current coordinate space in the grid.
            lattice_path_corners[x_2][y_2] = one_up + one_down

    routes = lattice_path_corners[grid_size][grid_size]
    return routes


if __name__ == "__main__":
    answer = problem_15()
    print(answer)
