from itertools import product, groupby
from typing import List


def prepare_adaptor_list(adaptors_list: List[int]):
    adaptors_list.append(0)
    adaptors_list.append(max(adaptors_list) + 3)
    return sorted(adaptors_list)


def process_adaptors(adaptors_list: List[int]):
    diffs = {"1": 0, "2": 0, "3": 0, "acc": []}

    for index, adaptor in enumerate(adaptors_list[1:]):
        diff = adaptor - adaptors_list[index]
        diffs["acc"].append(diff)
        diffs[str(diff)] = diffs[str(diff)] + 1

    return diffs


def count_all_arrangements_from_ones():
    for length in range(1, 10):
        arr = [1] * length
        arrangements = []

        r = range(0, 4)
        all_combs = list(
            product(
                r, repeat=length
            )  # Only cartesian product gives me all the possible combinations, with same number used multiple times
        )  # all possible permutations, but there are duplicates because of the 0s

        # remove 0s and duplicates
        possible_combs = []
        for comb in all_combs:
            co = [val for val in comb if val != 0]
            if co and co not in possible_combs:
                possible_combs.append([val for val in comb if val != 0])

        for comb in possible_combs:
            if sum(comb) == sum(arr):
                arrangements.append(comb)

        print(f"for length {length}, {len(arrangements)} arrangements")


def count_arrangements_from_ones(list_of_ones):
    length = len(list_of_ones)
    arrangements = []

    r = range(0, 4)
    all_combs = list(
        product(r, repeat=length)
    )  # all possible permutations, but there are duplicates because of the 0s

    # remove 0s and duplicates
    possible_combs = []
    for comb in all_combs:
        co = [val for val in comb if val != 0]
        if co and co not in possible_combs:
            possible_combs.append([val for val in comb if val != 0])

    for comb in possible_combs:
        if sum(comb) == sum(list_of_ones):
            arrangements.append(comb)

    return len(arrangements)


def get_series_of_ones(list_of_diffs):
    """
    Find the longest serie of one in the list
    pop it
    Recursively until there is no more ones
    """
    series_of_one = [list(g) for k, g in groupby(list_of_diffs) if k == 1]

    return series_of_one


if __name__ == "__main__":
    """
    Order the list, add 0 at the beginning and max+3 at the end
    Store the diff of each consecutive digits (I'll assume it's always 1,2 or 3)
    """

    with open("example", "r") as f:
        example_input = [int(line.rstrip()) for line in f]
    with open("example_2", "r") as f:
        example_2_input = [int(line.rstrip()) for line in f]
    with open("puzzle", "r") as f:
        puzzle_input = [int(line.rstrip()) for line in f]

    # tests
    sorted_list_e = prepare_adaptor_list(example_input.copy())
    diffs_example = process_adaptors(sorted_list_e)
    result_example = diffs_example["1"] * diffs_example["3"]
    assert result_example == 7 * 5

    sorted_list_e2 = prepare_adaptor_list(example_2_input.copy())
    diffs_example_2 = process_adaptors(sorted_list_e2)
    result_example_2 = diffs_example_2["1"] * diffs_example_2["3"]
    assert result_example_2 == 22 * 10

    # puzzle
    sorted_list = prepare_adaptor_list(puzzle_input.copy())
    diffs_puzzle = process_adaptors(sorted_list)
    result_puzzle = diffs_puzzle["1"] * diffs_puzzle["3"]
    print(f"part_1 - diffs {result_puzzle}")

    # part 2
    """
    NB there's only 1 and 3 diffs (disregard 2)
    Initially 1 possible combination
    Check the acc from the diffs, consecutive sets of 1s
    1, 1 -> 1,1 / 2 -> *2 comb
    1, 1, 1 -> 1,1,1 / 2, 1 / 1, 2 / 3 -> *4 comb ?
    1, 1, 1, 1 -> 1,1,1,1 / 2, 1, 1 / 1, 2, 1 / 1, 1, 2 / 2, 2 / 3, 1 / 1, 3 -> *6 comb ?
    1, 1, 1, 1  1 -> 1,1,1,1,1 / 2, 1, 1, 1 / 1, 2, 1, 1 / 1, 1, 2, 1 / 1, 1, 1, 2 / 2, 2, 1 / 2, 1, 2 / 1, 2, 2 / ...
    
    Don't know, let's try some brute force
    """

    # tests
    acc_ex = 1
    s_ones_ex = get_series_of_ones(diffs_example["acc"].copy())
    for ones in s_ones_ex:
        acc_ex *= count_arrangements_from_ones(ones)
    assert acc_ex == 8

    acc_ex_2 = 1
    s_ones_ex_2 = get_series_of_ones(diffs_example_2["acc"].copy())
    for ones in s_ones_ex_2:
        acc_ex_2 *= count_arrangements_from_ones(ones)
    assert acc_ex_2 == 19208

    # puzzle
    acc_puzzle = 1
    s_ones = get_series_of_ones(diffs_puzzle["acc"].copy())
    for ones in s_ones:
        acc_puzzle *= count_arrangements_from_ones(ones)
    print(f"part_2 - arrangements {acc_puzzle}")
