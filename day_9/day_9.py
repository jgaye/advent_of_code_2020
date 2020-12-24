from itertools import combinations


def check_sum(int_list, int_should_be_sum):
    for couple in combinations(int_list, 2):
        if int_should_be_sum == sum(couple):
            return True

    return False


def find_weakness(int_list, preambule_len):
    for index in range(preambule_len, len(int_list)):
        if not check_sum(int_list[index - preambule_len : index], int_list[index],):
            return int_list[index]


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, 1):
        yield iterable[ndx : ndx + n]


def find_batch_sum(input_list, sum_to_find):
    for batch_len in range(2, len(input_list)):
        for b in batch(input_list, batch_len):
            if sum(b) == sum_to_find:
                return list(b)


if __name__ == "__main__":
    """
    What would be an efficient way to get the sums of couple of numbers from a list
    """

    # tests
    with open("example", "r") as f:
        example_input = [int(line.rstrip()) for line in f]
    weakness_example = find_weakness(example_input, 5)
    assert weakness_example == 127

    # puzzle
    with open("puzzle", "r") as f:
        puzzle_input = [int(line.rstrip()) for line in f]
    weakness_puzzle = find_weakness(puzzle_input, 25)
    print(f"part_1 - weakness {weakness_puzzle}")

    # part 2
    """
    double recursions to do sums
    """

    # tests
    batch_result_example = find_batch_sum(example_input, weakness_example)
    result_example = min(batch_result_example) + max(batch_result_example)
    assert result_example == 62

    # puzzle
    batch_result = find_batch_sum(puzzle_input, weakness_puzzle)
    result = min(batch_result) + max(batch_result)
    print(f"part_2 - batch_result {result}")
