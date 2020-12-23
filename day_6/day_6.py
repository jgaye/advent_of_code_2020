def read_input(input_filename):
    groups = []
    agg_group = []

    with open(input_filename, "r") as f:
        for line in f:

            line = line.replace("\n", "")
            if not line.strip():
                groups.append(agg_group)
                agg_group = []
            else:
                agg_group.append(line)

        # handle last line
        if agg_group:
            groups.append(agg_group)

    return groups


def count_nb_yes(group):
    return len("".join(set(group)))


def anyone_answered_yes(group_answers):
    questions_per_groups = []
    for group in group_answers:
        group_count = count_nb_yes("".join(group))
        questions_per_groups.append(group_count)

    return sum(questions_per_groups)


def everyone_answered_yes(group_answers):
    questions_per_group = []

    for group in group_answers:
        candidates = list(group[0])

        for answers in group:
            for candidate in candidates.copy():
                if candidate not in answers:
                    candidates.remove(candidate)

        questions_per_group.append(len(candidates))

    return sum(questions_per_group)


if __name__ == "__main__":
    # tests
    example_input = read_input("example")
    assert anyone_answered_yes(example_input) == 11

    # puzzle
    puzzle_input = read_input("puzzle")
    print(f"part_1 - anyone answered yes {anyone_answered_yes(puzzle_input)}")

    assert everyone_answered_yes(example_input) == 6
    print(f"part_2 - everyone answered yes {everyone_answered_yes(puzzle_input)}")
