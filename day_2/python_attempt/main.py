from input import load_reports_from_file
from safty import is_safe


def main():
    print("Hello from python-attempt!")


def exercise_1():
    reports = load_reports_from_file("../input/reports.txt")
    safe_reports = [report for report in reports if is_safe(report)]
    print(f"There are {len(safe_reports)} safe reports")


if __name__ == "__main__":
    exercise_1()
    main()
