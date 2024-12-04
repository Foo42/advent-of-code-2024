from itertools import islice
from grid import Direction, Grid, load_grid_from_file


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
                candiate = list(islice(grid.values_along(coord, direction), len(word)))
                if candiate == target_list:
                    print(
                        f"Match at {coord.x},{coord.y} in direction {direction.as_cardinal()}"
                    )
                    matches += 1
    return matches


def exercise_1():
    grid = load_grid_from_file("../input/grid.txt")
    matches = count_word_in_grid("XMAS", grid)
    print(f'Found {matches} occurences of "XMAS"')


def main():
    exercise_1()


if __name__ == "__main__":
    main()
