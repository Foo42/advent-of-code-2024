from utils import make_pairs


def is_safe(report: list[int]) -> bool:
    pairs = make_pairs(report)
    deltas = [a - b for a, b in pairs]
    assert len(deltas) > 0
    is_ascending = deltas[0] > 0
    acceptable_range = range(1, 4) if is_ascending else range(-3, 0)
    return all(d in acceptable_range for d in deltas)
