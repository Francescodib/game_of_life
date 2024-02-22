import pygame
from state import get_initial_state, compute_new_state


l_size = 600
size = (l_size, l_size)
quantity:int = 120
cell_size= l_size / quantity

#Read seed.txt file, that contains the first death/live state of the grid
#you need to generate a new sed file if the quantity is upper than 500 by using che script generate_seed.py
with open("seed.txt", "r") as f:
    config = f.readlines()
    grid_state = get_initial_state(config,quantity)

pygame.init()
screen = pygame.display.set_mode(size)
is_running = True
clock = pygame.time.Clock()


def draw_cell(cell: bool, x: int, y: int) -> None:
    """
    Draws a single cell on the screen.

    Args:
        cell (bool): Whether the cell is alive or not.
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.

    Returns:
        None

    """
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    if cell:
        pygame.draw.rect(screen, "green3", rect)
    else:
        pygame.draw.rect(screen, "blue3", rect)


def draw_grid(grid: List[List[bool]]) -> None:
    """
    Draws the grid of cells on the screen.

    Args:
        grid (List[List[bool]]): The grid of cells, where each cell is represented by a boolean value indicating whether it is alive or not.

    Returns:
        None

    """
    for i in range(0, quantity):
        for j in range(0, quantity):
            draw_cell(grid[i][j], i, j)


# The code block inside the `while is_running:` loop is responsible for running the game of life
# simulation using Pygame. Here is a breakdown of what each step does:
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    grid_state = compute_new_state(grid_state,quantity)
    draw_grid(grid_state)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
