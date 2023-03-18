class Tile:
    value: str
    sides: list[int]

    def __init__(self, value: str, sides: list[int]) -> None:
        self.value = value
        self.sides = sides

    def __repr__(self) -> str:
        return self.value
