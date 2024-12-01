from input import parse
from distance import calculate_total_distance_of_closest

def exercise_1():
    lines = []
    with open('../input/lists.txt') as example_file:
        lines = example_file.readlines()
    pair_of_lists = parse(lines)
    total_distance = calculate_total_distance_of_closest(pair_of_lists)
    print(f'total distance: {total_distance}')


def main():
    exercise_1()


if __name__ == "__main__":
    main()
