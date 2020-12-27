from Day import Day


class Ship:
    """
    N -> positive y
    E -> positive x
    """

    def __init__(self, with_waypoint=False):
        self.location = [0, 0]
        self.direction = "E"
        if with_waypoint:
            self.waypoint = Waypoint()

    @classmethod
    def parse_instruction(cls, instruction):
        direction = instruction[0]
        value = int(instruction[1:])

        return direction, value

    def read_instruction(self, instruction, value):
        if instruction in ["L", "R"]:
            return self.turn(instruction, value)
        return self.move(instruction, value)

    def u_turn(self):
        if self.direction == "N":
            self.direction = "S"
        elif self.direction == "E":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "N"
        else:
            self.direction = "E"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "S"

    def turn(self, direction, value):
        if value in [360, 0]:
            pass
        elif value == 180:
            self.u_turn()
        elif value == 270:
            if direction == "R":
                self.turn_left()
            else:
                self.turn_right()
        else:
            if direction == "L":
                self.turn_left()
            else:
                self.turn_right()

        return self.location, self.direction

    def move(self, direction, value):
        if direction == "N":
            self.location[1] += value
        elif direction == "E":
            self.location[0] += value
        elif direction == "S":
            self.location[1] -= value
        elif direction == "W":
            self.location[0] -= value
        else:  # forward
            self.move(self.direction, value)
        return self.location, self.direction

    def m_dist(self):
        return abs(self.location[0]) + abs(self.location[1])

    # Part 2 below
    def move_towards_waypoint(self, value):
        w_loc = self.waypoint.location
        self.location[0] += value * w_loc[0]
        self.location[1] += value * w_loc[1]
        return self.location


class Waypoint(Ship):
    """
    location of the waypoint is relative to the ship
    """

    def __init__(self):
        super(Waypoint, self).__init__()
        self.location = [10, 1]

    def u_turn(self):
        self.location[0] = -self.location[0]
        self.location[1] = -self.location[1]
        return self.location

    def turn_left(self):
        tmp_x = self.location[0]
        tmp_y = self.location[1]
        self.location = [-tmp_y, tmp_x]
        return self.location

    def turn_right(self):
        tmp_x = self.location[0]
        tmp_y = self.location[1]
        self.location = [tmp_y, -tmp_x]
        return self.location


class Day12(Day):
    """
    part 1 strategy:
    Just follow the instructions to know the last coordinates

    part 2:
    The Ship class becomes the waypoint class
    A new Ship class is created
    A Ship has a waypoint
    When moving forward, use the waypoint relative location to go in the right direction
    """

    def __init__(self):
        self.unit_test()
        super(Day12, self).__init__()

    def unit_test(self):
        # moving
        m_ship = Ship()
        instructions = ["N1", "E1", "S1", "W1", "F1"]
        locations = [[0, 1], [1, 1], [1, 0], [0, 0], [1, 0]]
        for i, d in enumerate(instructions):
            m_ship.read_instruction(*m_ship.parse_instruction(d))
            assert m_ship.location == locations[i]

        # turning
        t_ship = Ship()
        instructions = [
            "R90",
            "F1",
            "L90",
            "F1",
            "L180",
            "F1",
            "R180",
            "F1",
            "L270",
            "F1",
            "R270",
            "F1",
        ]
        locations = [
            [0, 0],
            [0, -1],
            [0, -1],
            [1, -1],
            [1, -1],
            [0, -1],
            [0, -1],
            [1, -1],
            [1, -1],
            [1, -2],
            [1, -2],
            [2, -2],
        ]
        for i, d in enumerate(instructions):
            t_ship.read_instruction(*t_ship.parse_instruction(d))
            assert t_ship.location == locations[i]

    def run_example_part_1(self):
        expected_locations = iter([[10, 0], [10, 3], [17, 3], [17, 3], [17, -8]])

        ship = Ship()
        input = self.parse_input_file("example")

        for instruction in input:
            ship.read_instruction(*ship.parse_instruction(instruction))
            assert ship.location == next(expected_locations)

        assert ship.m_dist() == 25

    def run_puzzle_part_1(self):
        ship = Ship()
        input = self.parse_input_file("puzzle")

        for instruction in input:
            ship.read_instruction(*ship.parse_instruction(instruction))

        print(f"part 1 - m_dist {ship.m_dist()}")

    def run_puzzle_part_2(self):
        expected_locations = iter(
            [[100, 10], [100, 10], [170, 38], [170, 38], [214, -72]]
        )

        ship = Ship(with_waypoint=True)
        input = self.parse_input_file("example")

        for instruction in input:
            direction, value = ship.parse_instruction(instruction)
            if direction == "F":
                ship.move_towards_waypoint(value)
            else:
                ship.waypoint.read_instruction(direction, value)
            assert ship.location == next(expected_locations)

        assert ship.m_dist() == 286

    def run_example_part_2(self):
        ship = Ship(with_waypoint=True)
        input = self.parse_input_file("puzzle")

        for instruction in input:
            direction, value = ship.parse_instruction(instruction)
            if direction == "F":
                ship.move_towards_waypoint(value)
            else:
                ship.waypoint.read_instruction(direction, value)

        print(f"part 2 - m_dist {ship.m_dist()}")


if __name__ == "__main__":

    Day12()
