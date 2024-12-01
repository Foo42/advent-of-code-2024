from input import to_pair_of_lists


def match_closest(pairs: list[tuple[int,int]]) -> list[tuple[int, int]]:
    left_list, right_list = to_pair_of_lists(pairs)

    left_list.sort()
    right_list.sort()
    assert len(left_list) == len(right_list)
    return list(zip(left_list, right_list))


def calculate_total_distance_of_closest(pairs: list[tuple[int, int]]) -> int:
    closest_pairs = match_closest(pairs)
    distances = [abs(a-b) for (a,b) in closest_pairs ]
    return sum(distances)

