#!/bin/env python3

from tile import Tile
from grid import Grid


tiles: set[Tile] = set()
tiles.add(Tile('┌', [0, 1, 1, 0]))
tiles.add(Tile('┐', [0, 0, 1, 1]))
tiles.add(Tile('└', [1, 1, 0, 0]))
tiles.add(Tile('┘', [1, 0, 0, 1]))
tiles.add(Tile('┼', [1, 1, 1, 1]))
tiles.add(Tile(' ', [0, 0, 0, 0]))
tiles.add(Tile('│', [1, 0, 1, 0]))
tiles.add(Tile('─', [0, 1, 0, 1]))
tiles.add(Tile('├', [1, 1, 1, 0]))
tiles.add(Tile('┤', [1, 0, 1, 1]))
tiles.add(Tile('┬', [0, 1, 1, 1]))
tiles.add(Tile('┴', [1, 1, 0, 1]))
# tiles.add(Tile('╶', [0, 1, 0, 0]))
# tiles.add(Tile('╷', [0, 0, 1, 0]))
# tiles.add(Tile('═', [0, 2, 0, 2]))
# tiles.add(Tile('║', [2, 0, 2, 0]))
# tiles.add(Tile('╬', [2, 2, 2, 2]))
# tiles.add(Tile('╜', [2, 0, 0, 1]))
# tiles.add(Tile('╓', [0, 1, 2, 0]))
# tiles.add(Tile('╫', [2, 1, 2, 1]))
# tiles.add(Tile('╪', [1, 2, 1, 2]))


grid = Grid(120, 30, tiles)

# List contains entropy sorted references to grid tiles
sorted_grid: list[set[Tile]] = sorted(grid.grid, key=len)

while grid.observe_least_entropy():
    grid.propagate()

for y in range(grid.height):
    for x in range(grid.width):
        try:
            print(grid.get(x, y).pop(), end='')
        except:
            print('?', end='')
    print()
