def parse(lines: list[str]) -> list[tuple[int, int]]:
    pairs = [line.split() for line in lines]
    assert all([len(pair) == 2 for pair in pairs])
    numbers = [(int(pair[0]), int(pair[1])) for pair in pairs] 
    return numbers


def to_pair_of_lists(list_of_pairs: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    for (left, right) in list_of_pairs:
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list
