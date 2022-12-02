def get_input(input_file):
    with open(input_file, 'r') as input_file:
        input_string = input_file.read()
    return input_string


def get_points_result(match):
    values = match.split(" ")
    diff = ord(values[1]) - ord(values[0])
    points = -1
    if diff == 21:
        points = 6
    if diff == 22:
        points = 0
    if diff == 23:
        points = 3
    if diff == 24:
        points = 6
    if diff == 25:
        points = 0
    return points


def get_points_selection(match):
    selection = ord(match.split(" ")[1])
    points = -1
    if selection == 88:  # rock
        points = 1
    if selection == 89:  # paper
        points = 2
    if selection == 90:  # scissors
        points = 3
    return points


def get_points_match(match):
    return get_points_result(match) + get_points_selection(match)


def get_points_total_part_1(matches):
    points_total = 0
    for match in matches:
        points_total += get_points_match(match)
    return points_total


def transform_match(match):
    oppenent = match.split(" ")[0]
    oppenent_ord = ord(oppenent)
    result = match.split(" ")[1]

    my = 0
    if result == "X":
        my = oppenent_ord + 22
    if result == "Y":
        my = oppenent_ord + 23
    if result == "Z":
        my = oppenent_ord + 24

    if my == 91:
        my = 88

    if my == 87:
        my = 90

    my_chr = chr(my)

    return oppenent + " " + my_chr


def get_points_total_part_2(matches):
    points_total = 0
    for match in matches:
        points_total += get_points_match(transform_match(match))
    return points_total


def main():
    input_string = get_input("input.txt")
    matches = input_string.split("\n")

    # star 1
    print("Solution day 1, part 1: ", get_points_total_part_1(matches))

    # star 2
    print("Solution day 1, part 2: ", get_points_total_part_2(matches))


main()
