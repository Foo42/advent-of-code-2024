from itertools import islice
from grid import Direction, Grid, Vec2, load_grid_from_file


def count_word_in_grid(word: str, grid: Grid) -> int:
    target_list = list(word)
    directions = [
        Direction(0, 1),  # South
        Direction(1, 1),  # South East
        Direction(1, 0),  # East
        Direction(1, -1),  # North East
        Direction(0, -1),  # North
        Direction(-1, -1),  # North West
        Direction(-1, 0),  # West
        Direction(-1, 1),  # South West
    ]
    matches = 0
    for char, coord in grid.cells_by_row():
        if char == word[0]:
            for direction in directions:
                candiate = list(
                    grid.values_along(coord, direction, max_length=len(word))
                )
                if candiate == target_list:
                    print(
                        f"Match at {coord.x},{coord.y} in direction {direction.as_cardinal()}"
                    )
                    matches += 1
    return matches


def find_xmas_crosses(grid: Grid) -> int:
    south_east = Direction(1, 1)  # South East
    north_east = Direction(1, -1)  # North East
    matches = 0
    targets = [list("MAS"), list("SAM")]

    def in_bounds(coordinate: Vec2) -> bool:
        if (
            coordinate.x < 1 or coordinate.x > grid.size.x - 2
        ):  # -1 to go from a width to a 0-based coordinate, -2 because we want to be one away from the edige
            return False
        if coordinate.y < 1 or coordinate.y > grid.size.y - 2:
            return False
        return True

    possible_centres = [
        cell for cell in grid.cells_by_row() if cell[0] == "A" and in_bounds(cell[1])
    ]
    for _, coord in possible_centres:
        if list(grid.values_along(coord + Vec2(-1, -1), south_east, 3)) in targets:
            if list(grid.values_along(coord + Vec2(-1, 1), north_east, 3)) in targets:
                matches += 1
    return matches


def exercise_2():
    grid = load_grid_from_file("../input/grid.txt")
    matches = find_xmas_crosses(grid)
    print(f"Found {matches} X-MAS")


def exercise_1():
    grid = load_grid_from_file("../input/grid.txt")
    matches = count_word_in_grid("XMAS", grid)
    print(f'Found {matches} occurences of "XMAS"')


def main():
    exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()
