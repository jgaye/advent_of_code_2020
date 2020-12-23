import math
from sys import getsizeof


def find_coord(x, row):
    x = x % len(row)
    return row[x]


def go_down_slope(delta_x, delta_y, slope_map):
    nb_trees = 0
    expected_y_index = 0

    for y_index, slope_row in enumerate(slope_map):
        if y_index != expected_y_index:
            continue
        if find_coord(int((y_index * delta_x) / delta_y), slope_row) == "#":
            nb_trees += 1
        expected_y_index += delta_y
    return nb_trees


def list_vs_gen():
    """
    # Are generator really more memory efficient than lists ?
    # Starting at how many elements ?

    :return:
    """

    # with open("example_1", "r") as f:
    with open("puzzle_1", "r") as f:
        input_data_list = [line.rstrip() for line in f]
    input_data_gen = (x for x in input_data_list)

    print(
        f"""
        For length {len(input_data_list)}
        mem size of gen {getsizeof(input_data_gen)} bytes
        mem size of list {getsizeof(input_data_list)} bytes
    """
    )

    byte_sizes = []
    for index, elem in enumerate(input_data_list):
        if getsizeof((input_data_list[:index])) <= getsizeof(input_data_list[:index]):
            print(
                f"Generator takes less memory than list with {index+1} elem, with gen mem size {getsizeof((input_data_list[:index]))} "
            )
            break

    return input_data_list, input_data_gen


if __name__ == "__main__":

    input_data_list, input_data_gen = list_vs_gen()

    # starting point is (0,0)
    slope_map = input_data_gen

    print(f"part 1 - nb trees {go_down_slope(3,1, input_data_gen)}")

    # part 2
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    all_trees = []
    for slope in slopes:
        # using list because you can't reset a generator

        all_trees.append(go_down_slope(slope[0], slope[1], input_data_list))

    print(f"part 2 - nb trees total {math.prod(all_trees)}")
