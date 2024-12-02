from utils import make_pairs


def is_safe(report: list[int], problem_damping: bool = False) -> bool:
    pairs = make_pairs(report)
    deltas = [a - b for a, b in pairs]
    assert len(deltas) > 0
    is_ascending = deltas[0] > 0
    acceptable_range = range(1, 4) if is_ascending else range(-3, 0)
    problems_positions = [
        index for index, d in enumerate(deltas) if d not in acceptable_range
    ]
    if len(problems_positions) == 0:
        return True
    if not problem_damping:
        return False

    variations = [without_index(report, i) for i in range(0, len(report))]
    return any(is_safe(variation) for variation in variations)


def without_index[T](l: list[T], index: int) -> list[T]:
    return [item for i, item in enumerate(l) if i != index]
