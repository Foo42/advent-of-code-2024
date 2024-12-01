from input import load_from_file, parse
from distance import calculate_total_distance_of_closest, match_closest
from similarity import count_occurrences, calculate_similarity

def test_parse_line():
    input_lines = ['1   4', '5   7']
    expected_output = ([1,5], [4,7])
    assert parse(input_lines) == expected_output

def test_pair_closest():
    inputs = ([1, 20, 1, 2], [1, 21, 9, 3])
    expected = [(1,1), (1,3), (2,9), (20,21)]
    assert match_closest(inputs) == expected

def test_example_lists():
    pair_of_lists = load_from_file('../input/example.txt')
    total_distance = calculate_total_distance_of_closest(pair_of_lists)
    assert total_distance == 11

def test_count_occurances():
    target = 3
    others = [2,4,3,3,6,3,1,3]
    assert count_occurrences(target, others) == 4

def test_part_2_example():
    pair_of_lists = load_from_file('../input/example.txt')
    assert calculate_similarity(pair_of_lists) == 31
