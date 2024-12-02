from input import load_reports_from_file
from safty import is_safe


def exercise_1():
    reports = load_reports_from_file("../input/reports.txt")
    safe_reports = [report for report in reports if is_safe(report)]
    print(f"There are {len(safe_reports)} safe reports")


def exercise_2():
    reports = load_reports_from_file("../input/reports.txt")
    safe_reports = [
        report for report in reports if is_safe(report, problem_damping=True)
    ]
    print(f"There are {len(safe_reports)} safe reports with problem damping")


def main():
    exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()
