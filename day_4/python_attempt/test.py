from itertools import islice
from grid import coordinates_in_direction, load_grid_from_file, Vec2
from main import count_word_in_grid


def test_load_example_into_grid():
    grid = load_grid_from_file("../input/example.txt")
    assert len(list(grid.cells_by_row())) == 100  # 10 x 10 grid
    assert grid.value_at(Vec2(9, 9)) == "X"
    assert grid.value_at(Vec2(1, 2)) == "M"
    assert grid.value_at(Vec2(10, 10)) == None


def test_example():
    grid = load_grid_from_file("../input/example.txt")
    matches = count_word_in_grid("XMAS", grid)
    assert matches == 18
