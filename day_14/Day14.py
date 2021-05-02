import re
from typing import List

from Day import Day


class Bitmask(str):
    def __init__(self, string_of_bits: str):
        self.mask = string_of_bits.rjust(36, "X")

    def overwrite(self, int_value: int):
        bin_value = bin(int_value)[2:].rjust(36, "0")
        for i, m in enumerate(self.mask):
            if m != "X":
                l = list(bin_value)
                l[i] = m
                bin_value = "".join(l)
        return int(f"0b{bin_value}", 2)

    def overwrite_address(self, address: int) -> List[int]:
        bin_addresses = [bin(address)[2:].rjust(36, "0")]
        for i, m in enumerate(self.mask):
            results = []
            if m == "1":
                for a in bin_addresses:
                    l = list(a)
                    l[i] = m
                    results.append("".join(l))
            elif m == "X":
                for a in bin_addresses:
                    l1, l2 = list(a), list(a)
                    l1[i], l2[i] = "0", "1"
                    results.append("".join(l1))
                    results.append("".join(l2))
            elif m == "0":
                results = bin_addresses
            bin_addresses = results
        return [int(b, 2) for b in bin_addresses]


class Day14(Day):
    """

    """

    def __init__(self):
        super(Day14, self).__init__()

    def parse_input_file(self, filename):
        input = super(Day14, self).parse_input_file(filename)

        all_addresses = []
        for i in input:
            matches = re.findall(r"mem\[[0-9]*\]", i)
            if not matches:
                continue
            all_addresses.append(int(matches[0].replace("mem[", "").replace("]", "")))
        return input, [0] * (max(all_addresses) + 1)

    def run_part_1(self, filename):
        input, arr = self.parse_input_file(filename)

        for i in input:
            if i.startswith("mask = "):
                bitmask = Bitmask(i[7:])
            else:
                address, value = (
                    int(i.split("]")[0].replace("mem[", "")),
                    int(i.split("=")[1]),
                )
                arr[address] = bitmask.overwrite(value)

        print(sum(arr))

    def run_part_2(self, filename):
        input, arr = self.parse_input_file(filename)

        # the max address can increase so we should do a dict instead
        res = {}

        for i in input:
            if i.startswith("mask = "):
                bitmask = Bitmask(i[7:])
            else:
                address, value = (
                    int(i.split("]")[0].replace("mem[", "")),
                    int(i.split("=")[1]),
                )
                addresses = bitmask.overwrite_address(address)
                for a in addresses:
                    res[a] = value

        print(sum(res.values()))

    def run_example_part_1(self):
        self.run_part_1("example")

    def run_puzzle_part_1(self):
        self.run_part_1("puzzle")

    def run_example_part_2(self):
        self.run_part_2("example2")

    def run_puzzle_part_2(self):
        self.run_part_2("puzzle")


if __name__ == "__main__":
    Day14()
