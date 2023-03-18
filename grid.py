from tile import Tile
from random import choice


class Grid:
    width: int
    height: int
    grid: list[set[Tile]]

    def __init__(self, width: int, height: int, tiles: set[Tile]) -> None:
        self.width = width
        self.height = height
        self.grid = []
        for _ in range(height):
            for _ in range(width):
                self.grid.append(tiles.copy())

    def get(self, x: int, y: int) -> set[Tile]:
        return self.grid[y * self.width + x]

    def observe(self, x: int, y: int) -> None:
        options = list(self.get(x, y))
        if len(options) <= 1:
            return
        tile = choice(options)
        self.get(x, y).clear()
        self.get(x, y).add(tile)
        self.collapse(x, y)

    def intersect(self, x: int, y: int, other_x: int, other_y: int, side) -> None:
        options = self.get(other_x, other_y)
        if len(options) == 0:
            return

        connectors = [x.sides[side] for x in self.get(x, y)]

        old_len = len(options)

        options.intersection_update(
            [x for x in options if x.sides[side ^ 2] in connectors])

        if old_len != len(options):
            self.collapse(other_x, other_y)

    def collapse(self, x: int, y: int) -> None:
        if y > 0:
            self.intersect(x, y, x, y - 1, 0)
        if y < self.height - 1:
            self.intersect(x, y, x, y + 1, 2)
        if x > 0:
            self.intersect(x, y, x - 1, y, 3)
        if x < self.width - 1:
            self.intersect(x, y, x + 1, y, 1)
