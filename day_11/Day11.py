import os
from copy import deepcopy
from itertools import product
from typing import List

from Day import Day


class Day11(Day):
    seats: List[List[str]] = [[]]

    def __init__(self, input_filename=None, input_data=None):
        super().__init__(input_filename, input_data)
        self.seats = self.input_data
        try:
            self.room_width = len(self.seats[0])
            self.room_length = len(self.seats)
        except IndexError:
            # the room ha no widht and heigh
            self.room_width = 0
            self.room_length = 0

    def parse_input_file(self, filename):
        with open(filename, "r") as f:
            self.input_data = [list(line.rstrip()) for line in f]

    def count_occupied_seats(self) -> int:
        """
        Flatten seats
        Count #
        :return: nb of occupied seats
        """
        flattened_seats = [item for sublist in self.seats for item in sublist]
        return flattened_seats.count("#")

    def compare_seats_to_file(self, filename):
        with open(filename, "r") as f:
            candidate_data = [list(line.rstrip()) for line in f]
        return candidate_data == self.seats

    def get_surrounding_seats(self, x, y):
        """
        part 2 change
        need to know what is the direction of the seat, to maybe go get the next one in line
        So returning a dict instead of a list
        """
        dir_coord = {
            "NW": (x - 1, y - 1),
            "N": (x, y - 1),
            "NE": (x + 1, y - 1),
            "W": (x - 1, y),
            "E": (x + 1, y),
            "SW": (x - 1, y + 1),
            "S": (x, y + 1),
            "SE": (x + 1, y + 1),
        }
        surrounding_seats = {}

        for direction, coord in dir_coord.items():
            # do not keep coords outside of the room frame
            if 0 <= coord[0] < self.room_width and 0 <= coord[1] < self.room_length:
                surrounding_seats[direction] = {
                    "dist": 1,
                    "seat": self.seats[coord[1]][coord[0]],
                }

        return surrounding_seats

    def count_surrounding_occupied_seats(self, x, y):
        surrounding_seats = self.get_surrounding_seats(x, y)

        seats_only = [value["seat"] for value in surrounding_seats.values()]
        return seats_only.count("#")

    def check_dir_dist(self, x, y, direction, distance):
        if direction == "NW":
            coord = (x - distance, y - distance)
        elif direction == "N":
            coord = (x, y - distance)
        elif direction == "NE":
            coord = (x + distance, y - distance)
        elif direction == "W":
            coord = (x - distance, y)
        elif direction == "E":
            coord = (x + distance, y)
        elif direction == "SW":
            coord = (x - distance, y + distance)
        elif direction == "S":
            coord = (x, y + distance)
        else:
            coord = (x + distance, y + distance)

        # if out of the room frame, return a 'X' that will finish the outer loop
        # but not count as a occupied seat
        if not (0 <= coord[0] < self.room_width and 0 <= coord[1] < self.room_length):
            return "X"

        return self.seats[coord[1]][coord[0]]

    def count_visible_occupied_seats(self, x, y):
        visible_seats = self.get_surrounding_seats(x, y)

        for direction, params in visible_seats.items():
            while params["seat"] == ".":
                params["dist"] += 1
                params["seat"] = self.check_dir_dist(x, y, direction, params["dist"])

        seats_only = [value["seat"] for value in visible_seats.values()]
        return seats_only.count("#")

    def run_round(self):
        new_seats = deepcopy(self.seats)
        for row_index, row in enumerate(self.seats):
            for seat_index, seat in enumerate(row):
                if (
                    seat == "L"
                    and self.count_surrounding_occupied_seats(seat_index, row_index)
                    == 0
                ):
                    new_seats[row_index][seat_index] = "#"
                elif (
                    seat == "#"
                    and self.count_surrounding_occupied_seats(seat_index, row_index)
                    >= 4
                ):
                    new_seats[row_index][seat_index] = "L"

        self.seats = new_seats

    def run_round_part_2(self):
        new_seats = deepcopy(self.seats)
        for row_index, row in enumerate(self.seats):
            for seat_index, seat in enumerate(row):
                if (
                    seat == "L"
                    and self.count_visible_occupied_seats(seat_index, row_index) == 0
                ):
                    new_seats[row_index][seat_index] = "#"
                elif (
                    seat == "#"
                    and self.count_visible_occupied_seats(seat_index, row_index) >= 5
                ):
                    new_seats[row_index][seat_index] = "L"

        self.seats = new_seats


if __name__ == "__main__":
    """
    Trying to build a nice class for this day
    """

    example_cls = Day11(input_filename="example")
    # round 1
    example_cls.run_round()
    assert example_cls.compare_seats_to_file("example_round1")
    # round 2
    example_cls.run_round()
    assert example_cls.compare_seats_to_file("example_round2")
    # round 3
    example_cls.run_round()
    assert example_cls.compare_seats_to_file("example_round3")
    # round 4
    example_cls.run_round()
    assert example_cls.compare_seats_to_file("example_round4")
    # round 5
    example_cls.run_round()
    assert example_cls.compare_seats_to_file("example_round5")
    assert example_cls.count_occupied_seats() == 37

    # puzzle_cls = Day11(input_filename="puzzle")
    # previous_seats = [[]]
    # while puzzle_cls.seats != previous_seats:
    #     previous_seats = deepcopy(puzzle_cls.seats)
    #     puzzle_cls.run_round()
    # print(f"part 1 - nb occupied seats {puzzle_cls.count_occupied_seats()}")

    # part 2
    example_cls_p2 = Day11(input_filename="example")
    # round 1
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round1_part2")
    # round 2
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round2_part2")
    # round 3
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round3_part2")
    # round 4
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round4_part2")
    # round 5
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round5_part2")
    # round 5
    example_cls_p2.run_round_part_2()
    assert example_cls_p2.compare_seats_to_file("example_round6_part2")
    assert example_cls_p2.count_occupied_seats() == 26

    puzzle_cls_part_2 = Day11(input_filename="puzzle")
    previous_seats_part2 = [[]]
    while puzzle_cls_part_2.seats != previous_seats_part2:
        previous_seats_part2 = deepcopy(puzzle_cls_part_2.seats)
        puzzle_cls_part_2.run_round_part_2()
    print(f"part 2 - nb occupied seats {puzzle_cls_part_2.count_occupied_seats()}")
