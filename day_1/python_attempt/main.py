from input import load_from_file
from distance import calculate_total_distance_of_closest
from similarity import calculate_similarity

def exercise_1():
    pair_of_lists = load_from_file('../input/lists.txt')
    total_distance = calculate_total_distance_of_closest(pair_of_lists)
    print(f'total distance: {total_distance}')

def exercise_2():
    pair_of_lists = load_from_file('../input/lists.txt')
    similarity = calculate_similarity(pair_of_lists)
    print(f'total similarity: {similarity}')


def main():
    exercise_1()
    exercise_2()


if __name__ == "__main__":
    main()
