import copy


def get_stacks(stacks_string):
    stacks_strings = stacks_string.split('\n')
    stacks_strings.pop()
    stacks_strings = stacks_strings[::-1]
    stacks_amount = ((len(stacks_strings[0]) + 1) / 4)
    stack_counter = 1
    stacks = []
    while stack_counter <= stacks_amount:
        stack_index = stack_counter * 4 - 3
        full_stack = []
        for stack in stacks_strings:
            crate = stack[stack_index]
            if crate != ' ':
                full_stack.append(crate)
        stacks.append(full_stack)
        stack_counter += 1
    return stacks


def get_movements(movements_string):

    # Parse the movements
    movement_strings = movements_string.split('\n')
    movements = []
    for movement in movement_strings:
        _, crates_amount, _, from_stack, _, to_stack = movement.split(' ')
        movements.append((int(crates_amount), int(from_stack), int(to_stack)))
    return movements


def part_1(stacks, movements):

    stacks_copy = copy.deepcopy(stacks)

    # Perform the movements
    for crates_amount, from_stack, to_stack in movements:

        crates_counter = 1
        while crates_counter <= crates_amount:
            # Take the top crate from the from_stack
            crate = stacks_copy[from_stack - 1].pop()

            # Add the crate to the top of the to_stack
            stacks_copy[to_stack - 1].append(crate)

            crates_counter += 1

    # Print the top crate of each stack
    solution = ""
    for stack in stacks_copy:
        solution += (stack[-1])
    return solution


def part_2(stacks, movements):

    # Perform the movements
    for crates_amount, from_stack, to_stack in movements:

        # Take the top crate from the from_stack
        crates = stacks[from_stack - 1][-crates_amount:]
        stacks[from_stack - 1] = stacks[from_stack - 1][:len(stacks[from_stack - 1])-crates_amount]

        # Add the crate to the top of the to_stack
        stacks[to_stack - 1] += crates

    # Print the top crate of each stack
    solution = ""
    for stack in stacks:
        solution += (stack[-1])
    return solution


def main():

    # Read the input file and parse the initial configuration and the movements
    with open('input.txt') as input_file:
        # Parse the initial configuration of the stacks
        input_string = input_file.read()

    stacks_string, movements_string = input_string.split('\n\n')
    stacks = get_stacks(stacks_string)
    movements = get_movements(movements_string)

    print("Solution day 5, part 1: ", part_1(stacks, movements))
    print("Solution day 5, part 2: ", part_2(stacks, movements))


main()
