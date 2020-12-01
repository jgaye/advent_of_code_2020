if __name__ == '__main__':

    # with open("example_1", "r") as f:
    with open("puzzle_1", "r") as f:
        input_data = [int(line.rstrip()) for line in f]

    part_1_input = input_data.copy()
    for expense in part_1_input:
        # Looking for the 2020 complement directly
        if 2020-expense in input_data:
            print(f"part 1 : {expense * (2020-expense)}")
            break

        # if not found, you can remove the initial element to optimize consequent checks
        part_1_input.remove(expense)

    part_2_input = input_data.copy()
    for expense in part_2_input:
        for expense_2 in reversed(part_2_input):
            if 2020 - expense - expense_2 in input_data:
                print(f"part 2 : {expense * expense_2 * (2020 - expense - expense_2)}")
                break
        else:
            # Continue if the inner loop wasn't broken.
            # if not found, you can remove the initial element to optimize consequent checks
            part_2_input.remove(expense)
            continue
        # Inner loop was broken, break the outer.
        break
