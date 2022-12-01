def get_input():
    with open("input.txt",'r') as input_file:
        input = input_file.read()
    # print(input)
    return input


def get_elves_calories():
    elves = get_input().split("\n\n")
    # print(elves)

    elves_calories = []

    for elf in elves:
        calories = [int(calorie_string) for calorie_string in elf.split("\n")]
        elves_calories.append(sum(calories))
    # print(elves_calories)

    return elves_calories

def main():

    elves_calories = get_elves_calories()

    #star 1
    print("Solution day 1, part 1: ", max(elves_calories))
    
    #star 2
    elves_calories.sort(reverse=True)
    print("Solution day 1, part 2: ", sum(elves_calories[0:3]))

main()
