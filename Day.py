from abc import abstractmethod


class Day:
    def __init__(self):
        self.run_example_part_1()
        self.run_puzzle_part_1()
        self.run_example_part_2()
        self.run_puzzle_part_2()

    def parse_input_file(self, filename):
        with open(filename, "r") as f:
            input_data = [line.rstrip() for line in f]
        return input_data

    @abstractmethod
    def run_example_part_1(self):
        pass

    @abstractmethod
    def run_puzzle_part_1(self):
        pass

    @abstractmethod
    def run_example_part_2(self):
        pass

    @abstractmethod
    def run_puzzle_part_2(self):
        pass
