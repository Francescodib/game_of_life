
def get_initial_state(config,quantity):
    grid = []
    for i in range(0,quantity):
        row = []
        for j in range(0,quantity):
            cell = config[i][j] == "*"
            row.append(cell)
        grid.append(row)
    return grid


def get_neigbor_count(grid, x, y,quantity):
    return [
        is_live(grid, x - 1, y,quantity),
        is_live(grid, x + 1, y,quantity),
        is_live(grid, x, y - 1,quantity),
        is_live(grid, x, y + 1,quantity),
        is_live(grid, x - 1, y - 1,quantity),
        is_live(grid, x - 1, y + 1,quantity),
        is_live(grid, x + 1, y - 1,quantity),
        is_live(grid, x + 1, y + 1,quantity),
    ].count(True)


def compute_new_state(old_grid,quantity):
    grid = []
    for i in range(0,quantity):
        row = []
        for j in range(0,quantity):
            count = get_neigbor_count(old_grid, j, i,quantity)
            cell = count == 3 or count == 2 and old_grid[i][j]
            row.append(cell)
        grid.append(row)
    return grid


def is_live(grid, x, y,quantity):
    return is_within_bounds(x,quantity) and is_within_bounds(y,quantity) and grid[y][x]


def is_within_bounds(index,quantity):
    return index > 0 and index < (quantity)
