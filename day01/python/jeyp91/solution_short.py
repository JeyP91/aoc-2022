with open("input.txt", 'r') as input_file:
    elves_calories = list(map(lambda elf: sum([int(calorie_string) for calorie_string in elf.split("\n")]), input_file.read().split("\n\n")))
    elves_calories.sort(reverse=True)
    print("Solution day 1, part 1: ", max(elves_calories), "\nSolution day 1, part 2: ", sum(elves_calories[0:3]))
