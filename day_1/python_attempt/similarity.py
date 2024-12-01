def count_occurrences(target: int, others: list[int]) -> int:
    return len([x for x in others if x == target])

def calculate_similarity(pair_of_lists: tuple[list[int], list[int]]) -> int:
    left_list, right_list = pair_of_lists
    return sum([n * count_occurrences(n, right_list) for n in left_list])
