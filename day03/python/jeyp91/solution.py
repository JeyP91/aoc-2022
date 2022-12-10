from math import log2


def get_input(input_file):
    with open(input_file, 'r') as input_file:
        input_string = input_file.read()
    return input_string


def get_points_total_part_1(rucksacks):
    prio_sum = 0
    for rucksack in rucksacks:
        prio_sum += get_duplicate_prio(rucksack)
    return prio_sum


def get_points_total_part_2(rucksacks):
    element_counter = 0
    badges_sum = 0
    while element_counter < len(rucksacks):
        badge = get_badge(rucksacks[element_counter], rucksacks[element_counter+1], rucksacks[element_counter+2])
        badges_sum = badges_sum + badge
        element_counter = element_counter + 3
    return badges_sum


def char_to_prio(char):
    ascii_position = ord(char)
    if ascii_position > 93:
        return ascii_position - 96
    else:
        return ascii_position - 38


def bag_to_bitmap(bag):
    bitmap = 0
    for item in bag:
        bitmap = bitmap | (1 << (char_to_prio(item) - 1))
    return bitmap


def get_duplicate_prio(rucksack):
    bag_1 = rucksack[slice(0, len(rucksack)//2)]
    bag_2 = rucksack[slice(len(rucksack)//2, len(rucksack))]
    bag_1_bitmap = bag_to_bitmap(bag_1)
    bag_2_bitmap = bag_to_bitmap(bag_2)
    duplicate_bitmap = bag_1_bitmap & bag_2_bitmap
    return int(log2(duplicate_bitmap) + 1)


def get_badge(rucksack_1, rucksack_2, rucksack_3):
    rucksack_1_bitmap = bag_to_bitmap(rucksack_1)
    rucksack_2_bitmap = bag_to_bitmap(rucksack_2)
    rucksack_3_bitmap = bag_to_bitmap(rucksack_3)
    duplicate_bitmap = rucksack_1_bitmap & rucksack_2_bitmap & rucksack_3_bitmap
    return int(log2(duplicate_bitmap) + 1)


def main():
    input_string = get_input("input.txt")
    rucksacks = input_string.split("\n")

    # star 1
    print("Solution day 2, part 1: ", get_points_total_part_1(rucksacks))

    # star 2
    print("Solution day 2, part 2: ", get_points_total_part_2(rucksacks))


main()
