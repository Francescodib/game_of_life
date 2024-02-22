
def get_initial_state(config: List[List[str]], quantity: int) -> List[List[bool]]:
    """
    Returns a 2D list of booleans representing the initial game state.

    Parameters:
    -----------
    config: List[List[str]]
        The game configuration, where each element is a string of "*" and "." characters.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    grid: List[List[bool]]
        A 2D list of booleans representing the initial game state. Each element represents
        a cell in the grid, where True represents a live cell and False represents an empty cell.
    """
    grid = []
    for i in range(0, quantity):
        row = []
        for j in range(0, quantity):
            cell = config[i][j] == "*"
            row.append(cell)
        grid.append(row)
    return grid


def get_neigbor_count(grid: List[List[bool]], x: int, y: int, quantity: int) -> int:
    """
    Returns the number of live neighbours of a cell in the game grid.

    Parameters:
    -----------
    grid: List[List[bool]]
        The game grid, represented as a 2D list of booleans.
    x: int
        The x-coordinate of the cell.
    y: int
        The y-coordinate of the cell.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    count: int
        The number of live neighbours of the specified cell.

    """
    # Count the number of live neighbours of the specified cell
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if is_live(grid, i, j, quantity):
                count += 1
    return count


def is_live(grid: List[List[bool]], x: int, y: int, quantity: int) -> bool:
    """
    Returns a boolean indicating whether the specified cell is alive in the game grid.

    Parameters:
    -----------
    grid: List[List[bool]]
        The game grid, represented as a 2D list of booleans.
    x: int
        The x-coordinate of the cell.
    y: int
        The y-coordinate of the cell.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    is_live: bool
        A boolean indicating whether the specified cell is alive (True) or dead (False).

    """
    # Check if the specified cell is within bounds of the game grid
    if is_within_bounds(x, quantity) and is_within_bounds(y, quantity):
        # Return whether the specified cell is alive
        return grid[y][x]


def is_within_bounds(index: int, quantity: int) -> bool:
    """
    Returns a boolean indicating whether the specified index is within the bounds of the game grid.

    Parameters:
    -----------
    index: int
        The index to be checked.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    is_within_bounds: bool
        A boolean indicating whether the specified index is within the bounds of the game grid (True) or not (False).

    """
    # Check if the specified index is within the bounds of the game grid
    return 0 <= index < quantity


def compute_new_state(old_grid: List[List[bool]], quantity: int) -> List[List[bool]]:
    """
    Computes the next state of the Conway's Game of Life based on the current state.

    Parameters:
    -----------
    old_grid: List[List[bool]]
        The current state of the game grid, represented as a 2D list of booleans.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    grid: List[List[bool]]
        The next state of the game grid, represented as a 2D list of booleans.

    """
    grid = []
    for i in range(0, quantity):
        row = []
        for j in range(0, quantity):
            count = get_neigbor_count(old_grid, j, i, quantity)
            cell = count == 3 or count == 2 and old_grid[i][j]
            row.append(cell)
        grid.append(row)
    return grid


def is_live(grid: List[List[bool]], x: int, y: int, quantity: int) -> bool:
    """
    Returns a boolean indicating whether the specified cell is alive in the game grid.

    Parameters:
    -----------
    grid: List[List[bool]]
        The game grid, represented as a 2D list of booleans.
    x: int
        The x-coordinate of the cell.
    y: int
        The y-coordinate of the cell.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    is_live: bool
        A boolean indicating whether the specified cell is alive (True) or dead (False).

    """
    # Check if the specified cell is within bounds of the game grid
    if is_within_bounds(x, quantity) and is_within_bounds(y, quantity):
        # Return whether the specified cell is alive
        return grid[y][x]


def is_within_bounds(index: int, quantity: int) -> bool:
    """
    Returns a boolean indicating whether the specified index is within the bounds of the game grid.

    Parameters:
    -----------
    index: int
        The index to be checked.
    quantity: int
        The number of rows and columns in the game grid.

    Returns:
    --------
    is_within_bounds: bool
        A boolean indicating whether the specified index is within the bounds of the game grid (True) or not (False).

    """
    # Check if the specified index is within the bounds of the game grid
    return 0 <= index < quantity
