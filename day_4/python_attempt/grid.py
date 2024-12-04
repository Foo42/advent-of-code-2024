from collections.abc import Iterable, Iterator
from typing import NamedTuple, Self, Optional


class Vec2(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError()
        return Vec2(x=self.x + other.x, y=self.y + other.y)

    def __lt__(self, other):
        if not self.__class__ == other.__class__:
            raise TypeError()
        return self.x < other.x and self.y < other.y


class Direction(Vec2):
    def __init__(self, x: int, y: int):
        if abs(x) > 1 or abs(y) > 1:
            raise ValueError("Not a valid direction")

    def as_cardinal(self) -> str:
        match (self.y):
            case 1:
                n_s = "S"
            case -1:
                n_s = "N"
            case _:
                n_s = ""
        match (self.x):
            case 1:
                e_w = "E"
            case -1:
                e_w = "W"
            case _:
                e_w = ""
        return f"{n_s}{e_w}"


def coordinates_in_direction(start: Vec2, direction: Direction) -> Iterator[Vec2]:
    current = start
    while True:
        yield current
        current = current + direction


class Grid:
    def __init__(self, data: list[list[str]]):
        width = len(data[0])
        assert all(len(row) == width for row in data)
        self.data = data
        self.size = Vec2(x=width, y=len(data))

    def cells_by_row(self) -> Iterator[tuple[str, Vec2]]:
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                yield (cell, Vec2(x, y))

    def value_at(self, coordinates: Vec2) -> Optional[str]:
        if coordinates.x < 0 or coordinates.y < 0:
            return None
        if coordinates < self.size:
            return self.data[coordinates.y][coordinates.x]
        return None

    def values_along(self, start: Vec2, direction: Direction) -> Iterator[str]:
        path = coordinates_in_direction(start, direction)
        values = (self.value_at(coord) for coord in path)
        for value in values:
            if value is None:
                break
            yield value


def load_grid_from_file(path: str) -> Grid:
    lines: list[str] = []
    with open(path) as f:
        lines = f.readlines()
    return Grid([list(line.strip()) for line in lines])
