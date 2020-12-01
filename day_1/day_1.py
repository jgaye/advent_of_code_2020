import math
from typing import List


def look_for_complement(objective: int, candidates: List[int]):
    for element_1 in candidates:
        complement = objective - element_1
        if complement in candidates[1:]:
            return element_1, complement

        # if complement is not found, element_1 can be removed from the search
        candidates.remove(element_1)
    return None, None


if __name__ == "__main__":

    # with open("example_1", "r") as f:
    with open("puzzle_1", "r") as f:
        input_data = [int(line.rstrip()) for line in f]

    print(f"part 1 : {math.prod(look_for_complement(2020, input_data.copy()))}")

    part_2_input = input_data.copy()
    for element_1 in part_2_input:
        element_2, element_3 = look_for_complement(
            2020 - element_1, part_2_input[1:].copy()
        )
        if element_2:
            print(f"part 1 : {element_1*element_2*element_3}")
            break

        # if not found, you can remove the initial element to optimize consequent checks
        part_2_input.remove(element_1)
