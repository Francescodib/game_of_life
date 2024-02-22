import pygame
from state import get_initial_state, compute_new_state


l_size = 600
size = (l_size, l_size)
quantity:int = 120
cell_size= l_size / quantity

#read seed.txt file, that contains the first state of death/live 
#you need to generate a new sed file if the quantity is upper than 500 by using che script generate_seed.py

with open("seed.txt", "r") as f:
    config = f.readlines()
    grid_state = get_initial_state(config,quantity)

pygame.init()
screen = pygame.display.set_mode(size)
is_running = True
clock = pygame.time.Clock()


def draw_cell(cell, x, y):
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    if cell:
        pygame.draw.rect(screen, "green3", rect)
    else:
        pygame.draw.rect(screen, "blue3", rect)


def draw_grid(grid):
    for i in range(0,quantity):
        for j in range(0,quantity):
            draw_cell(grid[i][j], i, j)


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    grid_state = compute_new_state(grid_state,quantity)
    draw_grid(grid_state)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
