def run_instructions(instructions):
    ran_instructions_index = []
    current_index = 0
    instruction = instructions[current_index]
    acc = 0

    while current_index not in ran_instructions_index:
        ran_instructions_index.append(current_index)

        command = instruction[:3]
        val = int(instruction[3:])
        if command == "nop":
            current_index += 1
        elif command == "acc":
            acc += val
            current_index += 1
        elif command == "jmp":
            current_index += val

        instruction = instructions[current_index]

    return acc


def run_instructions_2(instructions):
    ran_instructions_index = []
    current_index = 0
    instruction = instructions[current_index]
    acc = 0

    try:
        while current_index not in ran_instructions_index:
            ran_instructions_index.append(current_index)

            command = instruction[:3]
            val = int(instruction[3:])
            if command == "nop":
                current_index += 1
            elif command == "acc":
                acc += val
                current_index += 1
            elif command == "jmp":
                current_index += val

            instruction = instructions[current_index]

        return False
    except IndexError:
        print(f"program finished successfully with {acc}")
        return acc


if __name__ == "__main__":
    """
    Looks simple enough to follow the instructions, with a while loop
    Keep a copy of all instructions ran, and if there is a duplicate, stop
    return the agg value"""

    # tests
    with open("example", "r") as f:
        example_input = [line.rstrip() for line in f]
    result = run_instructions(example_input)
    assert result == 5

    # puzzle
    with open("puzzle", "r") as f:
        puzzle_input = [line.rstrip() for line in f]
    result = run_instructions(puzzle_input)
    print(f"part_1 - result {result}")

    # part 2
    """
    If I exist from the part 1 function, I ddin;t really finish the code, so should replace one jmp to nop or vice versa then rerun instructions
    But if I have an index error, it means I got to the end of the instructions, and the result is ok
    """

    # tests
    for index, instruction in enumerate(example_input):
        if instruction.startswith("nop"):
            new_ints = example_input.copy()
            new_ints[index] = instruction.replace("nop", "jmp")
            result = run_instructions_2(new_ints)
            if result:
                break

        if instruction.startswith("jmp"):
            new_ints = example_input.copy()
            new_ints[index] = instruction.replace("jmp", "nop")
            result = run_instructions_2(new_ints)
            if result:
                break
    assert result == 8

    # puzzle
    for index, instruction in enumerate(puzzle_input):
        if instruction.startswith("nop"):
            new_ints = puzzle_input.copy()
            new_ints[index] = instruction.replace("nop", "jmp")
            result = run_instructions_2(new_ints)
            if result:
                break

        if instruction.startswith("jmp"):
            new_ints = puzzle_input.copy()
            new_ints[index] = instruction.replace("jmp", "nop")
            result = run_instructions_2(new_ints)
            if result:
                break
