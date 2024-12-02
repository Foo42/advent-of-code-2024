def make_pairs[T](l: list[T]) -> list[tuple[T, T]]:
    return list(zip(l, l[1:]))
