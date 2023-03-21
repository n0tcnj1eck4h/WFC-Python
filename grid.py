from tile import Tile
from random import choice


class Grid:
    width: int
    height: int
    grid: list[set[Tile]]
    propagation_queue: list[tuple[int, int]]
    sorted_grid: list[set[Tile]]
    wrap_around: bool

    def __init__(self, width: int, height: int, tiles: set[Tile]) -> None:
        self.width = width
        self.height = height
        self.grid = []
        for _ in range(height):
            for _ in range(width):
                self.grid.append(tiles.copy())
        self.sorted_grid = sorted(self.grid, key=len)
        self.propagation_queue = []
        self.wrap_around = True

    def get(self, x: int, y: int) -> set[Tile]:
        return self.grid[y * self.width + x]

    def observe_least_entropy(self) -> bool:
        self.sorted_grid.sort(key=len)

        # Pop all collapsed cells
        while len(self.sorted_grid) != 0 and len(self.sorted_grid[0]) <= 1:
            self.sorted_grid.pop(0)

        if len(self.sorted_grid) == 0:
            return False

        option = self.sorted_grid.pop(0)
        i = self.grid.index(option)
        self.observe(i % self.width, i // self.width)
        return True

    def observe(self, x: int, y: int) -> None:
        options = list(self.get(x, y))
        if len(options) <= 1:
            return
        tile = choice(options)
        self.get(x, y).clear()
        self.get(x, y).add(tile)
        self.propagation_queue.append((x, y))

    def intersect(self, x: int, y: int, other_x: int, other_y: int, side) -> None:
        options = self.get(other_x, other_y)
        if len(options) == 0:
            return

        connectors = {x.sides[side] for x in self.get(x, y)}

        old_len = len(options)

        options.intersection_update(
            {x for x in options if x.sides[side ^ 2] in connectors})

        if old_len != len(options):
            self.propagation_queue.append((other_x, other_y))

    def propagate(self):
        while len(self.propagation_queue):
            (x, y) = self.propagation_queue.pop()
            if self.wrap_around:
                self.intersect(x, y, x, (y - 1) % self.height, 0)
                self.intersect(x, y, x, (y + 1) % self.height, 2)
                self.intersect(x, y, (x - 1) % self.width, y, 3)
                self.intersect(x, y, (x + 1) % self.width, y, 1)
            else:
                if y > 0:
                    self.intersect(x, y, x, y - 1, 0)
                if y < self.height - 1:
                    self.intersect(x, y, x, y + 1, 2)
                if x > 0:
                    self.intersect(x, y, x - 1, y, 3)
                if x < self.width - 1:
                    self.intersect(x, y, x + 1, y, 1)
