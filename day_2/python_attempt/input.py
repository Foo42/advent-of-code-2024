def parse_report(line: str) -> list[int]:
    return [int(part) for part in line.split()]


def load_reports_from_file(path: str) -> list[list[int]]:
    lines: list[str] = []
    with open(path) as f:
        lines = f.readlines()
    return [parse_report(line) for line in lines]
