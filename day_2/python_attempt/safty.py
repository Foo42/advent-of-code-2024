from utils import make_pairs


def is_safe(report: list[int]) -> bool:
    pairs = make_pairs(report)
    deltas = [a - b for a, b in pairs]
    assert len(deltas) > 0
    is_ascending = deltas[0] > 0
    if is_ascending:
        if not all(delta > 0 for delta in deltas):
            return False
    else:
        if not all(delta < 0 for delta in deltas):
            return False

    absolute_deltas = [abs(delta) for delta in deltas]
    return all(d >= 1 and d <= 3 for d in absolute_deltas)
