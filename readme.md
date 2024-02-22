# Game of Life

This is a simple implementation of the Conway's Game of Life in Python.

## Requirements

- Python 3.6 or higher

## Installation

To install the required dependencies, in this case only pygame:

```bash
pip install pygame
```

## Usage

To run the game, simply execute the `main.py` file:

```bash
python main.py
```

## How to Play

The game is played on a grid of cells, where each cell can be either alive or dead. The objective of the game is to keep the grid alive by following the following rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The game is over when there are no more live cells on the grid.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.