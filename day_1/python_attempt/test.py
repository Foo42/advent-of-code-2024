from input import parse
from distance import calculate_total_distance_of_closest, match_closest

def test_parse_line():
    input_lines = ['1   4', '5   7']
    expected_output = ([1,5], [4,7])
    assert parse(input_lines) == expected_output

def test_pair_closest():
    inputs = ([1, 20, 1, 2], [1, 21, 9, 3])
    expected = [(1,1), (1,3), (2,9), (20,21)]
    assert match_closest(inputs) == expected

def test_example_lists():
    lines = []
    with open('../input/example.txt') as example_file:
        lines = example_file.readlines()
    pair_of_lists = parse(lines)
    total_distance = calculate_total_distance_of_closest(pair_of_lists)
    assert total_distance == 11
