from itertools import combinations
from math import gcd, prod

from Day import Day


class Bus:
    def __init__(self, id):
        self.id = id

    def get_last_departure_before_timestamp(self, timestamp):
        return (timestamp // self.id) * self.id

    def get_first_departure_after_timestamp(self, timestamp):
        return self.get_last_departure_before_timestamp(timestamp) + self.id

    def has_departure_at_timestamp(self, timestamp):
        return timestamp % self.id == 0


class Day13(Day):
    """
    part 1 strategy:
    We want the first timestamp AFTER my input timestamp
    For each bus multiplication table.
    Naive way : while loop for each bus id * index, until it is higher than my timestamp, then take the min of all the results
    Smarter way : get the index for the departure just BEFORE my timestamp with a floor division.
        Then do (i+1)*bus id - timestamp. Take the min of all results.

    part 2 strategy:
    Naive approach : brute force with a loop on the first bue of the list. For each departure of that bus, check if one minute after the next bus has a departure, etc.
        If not go back to the first bus, and check the next departure. etc....
    Smarter approach : similar to naive, but use the departure times of the bus with the highest bus_id (there will be less departure times to check !
        Also, use the clue that the timestamp will be larger than '100000000000000'
        -> I've ran this and it's very slow (10 minutes and no result for puzzle data)
    Smarter approach 2 : t = bus_id * x - bus_index, so (count_buses)*t = sum(bus_id*a factor - bus_index)
        So I can try all combination of (count_buses) factors as base_timestamp
    Super smart approach : there must be some maths that can give relations between all the bus_ids denominators... But the reseach might be longer than the smarter approach.
        -> My other methods are not efficient enough, so I looked into a hint on reddit, and learned about the https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_restes_chinois
        t is x from the theorem, let's implement this
        -> I had to use someone elses implem because my implem with the bezout coefs would not return the minimal response
    """

    def __init__(self):
        super(Day13, self).__init__()

    def parse_input_file(self, filename):
        timestamp, buses = super(Day13, self).parse_input_file(filename)
        return int(timestamp), buses.split(",")

    @staticmethod
    def get_next_departures(buses, timestamp):
        next_departures = {}
        for bus_id in buses:
            if bus_id != "x":
                bus = Bus(int(bus_id))
                next_departures[
                    bus.get_first_departure_after_timestamp(timestamp)
                ] = bus

        next_departure = min(next_departures)
        next_bus: Bus = next_departures[next_departure]

        return next_bus, next_departure

    def run_example_part_1(self):
        expected_result = 295

        timestamp, buses = self.parse_input_file("example")
        next_bus, next_departure = self.get_next_departures(buses, timestamp)

        assert next_bus.id * (next_departure - timestamp) == expected_result

    def run_puzzle_part_1(self):
        timestamp, buses = self.parse_input_file("puzzle")
        next_bus, next_departure = self.get_next_departures(buses, timestamp)

        print(f"part 1 - {next_bus.id * (next_departure - timestamp)}")

    @staticmethod
    def timestamp_works(t_after_timestamp, base_timestamp):
        found = True
        for bus_id in t_after_timestamp:
            bus = Bus(bus_id)
            if not bus.has_departure_at_timestamp(
                base_timestamp + t_after_timestamp[bus_id]
            ):
                found = False
                break

        return found

    def test_factors(self, bus_list, factors):
        highest_bus_id = max(bus_list)
        highest_bus_index = bus_list[highest_bus_id]

        base_timestamp = 0
        for factor in factors:
            base_timestamp = highest_bus_id * factor - highest_bus_index

            found = self.timestamp_works(bus_list, base_timestamp)
            if found:
                break

        return base_timestamp

    def find_base_timestamp(self, buses, minimum_timestamp):
        t_after_timestamp = {}
        for index, bus_id in enumerate(buses):
            if bus_id != "x":
                t_after_timestamp[int(bus_id)] = index

        highest_bus_id = max(t_after_timestamp)
        minimum_factor = minimum_timestamp // highest_bus_id

        # up to a million factors, it's decent perf, so I could parallelize this
        return self.test_factors(
            t_after_timestamp, range(minimum_factor, minimum_factor + 1000001)
        )

    @staticmethod
    def get_gcd(int_1, int_2):
        return gcd(int_1, int_2)

    @staticmethod
    def bezout(a, b):
        if b == 0:
            return 1, 0
        else:
            u, v = Day13.bezout(b, a % b)

        return v, u - (a // b) * v

    def chinese_remainder_theorem(self, rests, mods):
        for couple in combinations(mods, 2):
            if self.get_gcd(*couple) != 1:
                print(f"ERROR {couple} are not pairwise coprimes")

        n = prod(mods)

        x = 0
        for index, mod in enumerate(mods):
            ni = mod

            bi = (ni - rests[index]) % ni

            n_inv = n // ni

            c = n_inv % ni

            xi = 1
            while (c * xi) % ni != 1:
                xi += 1

            x += bi * n_inv * xi

        return x % n

    def run_example_part_2(self):
        expected_result = 1068781

        timestamp, buses = self.parse_input_file("example")
        # timestamp, buses = 0, ["3", "x", "x", "4", "5"]

        rests = []
        mods = []
        for index, bus_id in enumerate(buses):
            if bus_id != "x":
                mods.append(int(bus_id))
                rests.append(index)

        crt = self.chinese_remainder_theorem(rests, mods)

        # naive
        # base_timestamp = self.find_base_timestamp(buses, 0)

        assert crt == expected_result

    def run_puzzle_part_2(self):
        # pass
        timestamp, buses = self.parse_input_file("puzzle")

        rests = []
        mods = []
        for index, bus_id in enumerate(buses):
            if bus_id != "x":
                mods.append(int(bus_id))
                rests.append(index)

        crt = self.chinese_remainder_theorem(rests, mods)

        print(f"part 2 - {crt}")


if __name__ == "__main__":

    Day13()
