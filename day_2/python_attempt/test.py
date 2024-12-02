from utils import make_pairs
from safty import is_safe
from input import load_reports_from_file, parse_report


def test_parse_line():
    line = "2 4 7 43"
    expected = [2, 4, 7, 43]
    assert parse_report(line) == expected


def test_pairs():
    input = [1, 4, 5]
    expected = [(1, 4), (4, 5)]
    assert make_pairs(input) == expected


def test_example_data():
    reports = load_reports_from_file("../input/example.txt")
    safe_reports = [
        row_number for row_number, report in enumerate(reports, 1) if is_safe(report)
    ]
    assert safe_reports == [1, 6]
