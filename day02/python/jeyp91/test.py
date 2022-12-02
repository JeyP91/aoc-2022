from solution import get_points_result, get_input, get_points_selection, get_points_match, get_points_total_part_1, transform_match, \
    get_points_total_part_2


def test():
    input_string = get_input("input_test.txt")
    matches = input_string.split("\n")

    assert get_points_result(matches[0]) == 6  # A Y -> Rock - Paper -> Win
    assert get_points_result(matches[1]) == 0  # B X -> Paper - Rock -> Loss
    assert get_points_result(matches[2]) == 3  # C Z -> Scissors - Scissors -> Draw
    assert get_points_result("C X") == 6  # Scissors - Rock -> Win
    assert get_points_result("A Z") == 0  # Rock - Scissors -> Loss

    assert get_points_selection(matches[0]) == 2  # A Y -> Paper -> 2
    assert get_points_selection(matches[1]) == 1  # B X -> Rock -> 1
    assert get_points_selection(matches[2]) == 3  # C Z -> Scissors -> 3

    assert get_points_match(matches[0]) == 8
    assert get_points_match(matches[1]) == 1
    assert get_points_match(matches[2]) == 6

    assert get_points_total_part_1(matches) == 15

    assert transform_match(matches[0]) == "A X"
    assert transform_match(matches[1]) == "B X"
    assert transform_match(matches[2]) == "C X"

    assert get_points_total_part_2(matches) == 12

    print("Tests completed.")


test()
