import re

if __name__ == "__main__":

    # with open("example_1", "r") as f:
    with open("puzzle_1", "r") as f:
        input_data = [line.rstrip() for line in f]

    valid_pwds_part_1 = []
    valid_pwds_part_2 = []

    for row in input_data:
        rule, pwd = row.split(":")
        char_range, letter = rule.split(" ")
        char_min, char_max = [int(x) for x in char_range.split("-")]

        # part 1
        if char_min <= len(re.findall(letter, pwd)) <= char_max:
            valid_pwds_part_1.append(row)

        # part 2
        pos_1, pos2 = char_min, char_max
        characs_to_check = f"{pwd[pos_1]}{pwd[pos2]}"

        if len(re.findall(letter, characs_to_check)) == 1:
            valid_pwds_part_2.append(row)

    print(f"part 1 - nb valid passwords {len(valid_pwds_part_1)}")
    print(f"part 2 - nb valid passwords {len(valid_pwds_part_2)}")
