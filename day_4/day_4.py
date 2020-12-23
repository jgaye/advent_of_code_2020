import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_FIELDS = {"cid"}


def validate_passport(passport_candidate):
    has_required = REQUIRED_FIELDS <= passport_candidate.keys()
    has_optional = OPTIONAL_FIELDS <= passport_candidate.keys()
    return has_required, has_optional


def input_to_dict(input_line):
    result_dict = {}

    params = input_line.split(" ")
    for param in params:
        k, v = param.split(":")
        result_dict[k] = v

    return result_dict


def read_input(input_filename):
    input_data = []
    agg_line = ""

    with open(input_filename, "r") as f:
        for line in f:
            line = line.replace("\n", " ")
            if not line.strip():
                input_data.append(input_to_dict(agg_line.rstrip()))
                agg_line = ""
            else:
                agg_line = agg_line + line

        # handle last line
        if agg_line:
            input_data.append(input_to_dict(agg_line))

    return input_data


def validate_byr(byr):
    return 1920 <= int(byr) <= 2002


def validate_hgt(hgt):
    return ("cm" in hgt and 150 <= int(hgt[:-2]) <= 193) or (
        "in" in hgt and 59 <= int(hgt[:-2]) <= 76
    )


def validate_hcl(hcl):
    pattern_hcl = re.compile("#[0-9a-f]{6}")
    return pattern_hcl.fullmatch(hcl)


def validate_ecl(ecl):
    return ecl in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]


def validate_pid(pid):
    pattern_pid = re.compile("[0-9]{9}")
    return pattern_pid.fullmatch(pid)


def validate_passport_2(passport_candidate):
    if not REQUIRED_FIELDS <= passport_candidate.keys():
        return False

    if not validate_byr(passport_candidate["byr"]):
        return False

    if not validate_hgt(passport_candidate["hgt"]):
        return False

    if not validate_hcl(passport_candidate["hcl"]):
        return False

    if not validate_ecl(passport_candidate["ecl"]):
        return False

    if not validate_pid(passport_candidate["pid"]):
        return False

    if not 2010 <= int(passport_candidate["iyr"]) <= 2020:
        return False

    if not 2020 <= int(passport_candidate["eyr"]) <= 2030:
        return False

    return True


def count_valid_passports(list_input):
    nb_valid_passports = 0
    nb_full_passports = 0

    for passport_candidate in list_input:
        req, opt = validate_passport(passport_candidate)
        if req:
            nb_valid_passports += 1
            if opt:
                nb_full_passports += 1

    return nb_valid_passports


def count_valid_passports_2(list_input):
    nb_valid_passports = 0

    for passport_candidate in list_input:
        if validate_passport_2(passport_candidate):
            nb_valid_passports += 1

    return nb_valid_passports


if __name__ == "__main__":
    # tests
    example_1_input = read_input(input_filename="example_1")
    assert count_valid_passports(example_1_input) == 2

    example_2_input = read_input(input_filename="example_2")
    assert count_valid_passports_2(example_2_input) == 4

    assert validate_byr("2002")
    assert not validate_byr("2003")
    assert validate_hgt("60in")
    assert validate_hgt("190cm")
    assert not validate_hgt("190in")
    assert not validate_hgt("190")
    assert validate_hcl("#123abc")
    assert not validate_hcl("#123abz")
    assert not validate_hcl("123abc")
    assert validate_ecl("brn")
    assert not validate_ecl("wat")
    assert validate_pid("000000001")
    assert not validate_pid("0123456789")

    puzzle_1_input = read_input(input_filename="puzzle_1")
    valid_passport_1 = count_valid_passports(puzzle_1_input)
    print(f"part 1 - nb valid passports {valid_passport_1}")

    valid_passport_2 = count_valid_passports_2(puzzle_1_input)
    print(f"part 2 - nb valid passports {valid_passport_2}")
