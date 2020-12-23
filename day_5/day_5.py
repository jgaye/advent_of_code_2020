from math import floor, ceil


def parse_letter(letter, min, max):
    if letter == "F" or letter == "L":
        return min, floor((max + min) / 2)
    if letter == "B" or letter == "R":
        return ceil((max + min) / 2), max


def find_seat(boarding_pass):
    r_min = 0
    r_max = 127
    for letter in boarding_pass[:-3]:
        r_min, r_max = parse_letter(letter, r_min, r_max)

    c_min = 0
    c_max = 7
    for letter in boarding_pass[-3:]:
        c_min, c_max = parse_letter(letter, c_min, c_max)

    row = r_min
    column = c_min
    return row, column, row * 8 + column


if __name__ == "__main__":
    # tests
    example_1_input = "FBFBBFFRLR"
    assert find_seat(example_1_input) == (44, 5, 357)
    example_2_input = "BFFFBBFRRR"
    assert find_seat(example_2_input) == (70, 7, 567)
    example_3_input = "FFFBBBFRRR"
    assert find_seat(example_3_input) == (14, 7, 119)
    example_4_input = "BBFFBBFRLL"
    assert find_seat(example_4_input) == (102, 4, 820)

    # puzzle
    with open("puzzle", "r") as f:
        puzzle_input = [line.rstrip() for line in f]

    seat_ids = []
    for boarding_pass in puzzle_input:
        _, _, seat_id = find_seat(boarding_pass)
        seat_ids.append(seat_id)

    seat_ids = sorted(seat_ids)
    print(f"part_1 - highest seat_id {max(seat_ids)}")

    # the first (0) and last (max(seat_ids)) are not ours
    for seat_id_candidate in range(1, max(seat_ids)):
        if (
            seat_id_candidate not in seat_ids
            and seat_id_candidate - 1 in seat_ids
            and seat_id_candidate + 1 in seat_ids
        ):
            print(f"part_2 - our seat_id {seat_id_candidate}")
