def match_closest(pair_of_lists: tuple[list[int], list[int]]) -> list[tuple[int, int]]:
    left_list, right_list = pair_of_lists

    left_list.sort()
    right_list.sort()
    assert len(left_list) == len(right_list)
    return list(zip(left_list, right_list))


def calculate_total_distance_of_closest(pair_of_lists: tuple[list[int], list[int]]) -> int:
    closest_pairs = match_closest(pair_of_lists)
    distances = [abs(a-b) for (a,b) in closest_pairs ]
    return sum(distances)

