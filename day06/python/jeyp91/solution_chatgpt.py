def find_marker(input_string, length):
    # Iterate through the string, starting from the first character
    for i in range(len(input_string) - length):
        # Get the four characters starting at this position
        four_chars = input_string[i:i+length]

        # If there are four different characters in these four characters,
        # return the position where they start
        if len(set(four_chars)) == length:
            return i+length

    # If no four different characters were found, return -1
    return -1


def main():

    # Read the input file and parse the initial configuration and the movements
    with open('input.txt') as input_file:
        # Parse the initial configuration of the stacks
        input_string = input_file.read()

    print("Solution day 6, part 1: ", find_marker(input_string, 4))
    print("Solution day 6, part 2: ", find_marker(input_string, 14))


main()
