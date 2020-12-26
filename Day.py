class Day:
    input_data = None

    def __init__(self, input_filename=None, input_data=None):
        if input_filename:
            self.parse_input_file(input_filename)
        else:
            self.input_data = input_data

    def parse_input_file(self, filename):
        with open(filename, "r") as f:
            self.input_data = [line.rstrip() for line in f]
