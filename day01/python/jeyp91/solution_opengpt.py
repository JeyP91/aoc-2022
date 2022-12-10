# Open the input file
with open('input.txt') as file:
    # Create a list to store the number of Calories for each Elf
    calories = [0]

    # Create a variable to keep track of the maximum number of Calories for any Elf
    max_calories = 0

    # Create a variable to keep track of which Elf is carrying the most Calories
    max_elf = 0

    # Read the lines from the file
    lines = file.readlines()

    # Loop through each line in the file
    for line in lines:
        # If the line is blank, start a new entry in the calories list
        if line.strip() == '':
            calories.append(0)
        else:
            # Add the number of Calories to the current Elf's total
            calories[-1] += int(line.strip())
            # Update the maximum number of Calories and the corresponding Elf if necessary
            if calories[-1] > max_calories:
                max_calories = calories[-1]
                max_elf = len(calories)

# Print the results
print("The Elf carrying the most Calories is Elf #" + str(max_elf) + " with a total of " + str(max_calories) + " Calories.")
