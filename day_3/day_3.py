import math


def find_coord(x, y, map):
    x = x % len(map[0])
    return map[y][x]


if __name__ == "__main__":

    with open("example_1", "r") as f:
    # with open("puzzle_1", "r") as f:
        input_data = [line.rstrip() for line in f]

    # starting point becomes (0,0)
    slope_map = input_data
    map_width = len(slope_map[0])
    map_height = len(slope_map)

    index = 0
    nb_trees = 0

    # part 1
    while index < map_height:
        if find_coord(index*3, index, slope_map) == "#":
            nb_trees += 1
        index += 1
    print(f"part 1 - nb trees {nb_trees}")

    # part 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    all_trees = []
    for slope in slopes:

        index = 0
        nb_trees = 0

        while index < map_height-1:
            if find_coord(index*slope[0], index, slope_map) == "#":
                nb_trees += 1
            index += slope[1]
        all_trees.append(nb_trees)

    print(f"part 2 - nb trees total {math.prod(all_trees)}")
