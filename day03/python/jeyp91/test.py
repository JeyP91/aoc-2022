from solution import get_input, char_to_prio, bag_to_bitmap, get_duplicate_prio, get_points_total_part_1, get_badge, \
    get_points_total_part_2


def test():
    input_string = get_input("input_test.txt")
    rucksacks = input_string.split("\n")

    assert char_to_prio("a") == 1
    assert char_to_prio("A") == 27
    assert bag_to_bitmap("ab") == 3
    assert bag_to_bitmap("Z") == 2251799813685248
    assert bag_to_bitmap("aZ") == 2251799813685249
    assert bag_to_bitmap("Za") == 2251799813685249
    assert get_duplicate_prio(rucksacks[0]) == 16
    assert get_duplicate_prio(rucksacks[1]) == 38
    assert get_duplicate_prio(rucksacks[2]) == 42
    assert get_duplicate_prio(rucksacks[3]) == 22
    assert get_duplicate_prio(rucksacks[4]) == 20
    assert get_duplicate_prio(rucksacks[5]) == 19
    assert get_points_total_part_1(rucksacks) == 157

    assert get_badge(rucksacks[0], rucksacks[1], rucksacks[2]) == 18
    assert get_badge(rucksacks[3], rucksacks[4], rucksacks[5]) == 52
    assert get_points_total_part_2(rucksacks) == 70

    print("Tests completed.")


test()
