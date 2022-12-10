# read the input file
with open('input.txt', 'r') as file:
    assignments = file.readlines()

# remove leading and trailing whitespace from each line
assignments = [assignment.strip() for assignment in assignments]

# initialize a counter to keep track of the number of pairs
# where one range fully contains the other
counter_part_1 = 0
counter_part_2 = 0

# iterate over all pairs of assignments
for pair in assignments:
    # split each assignment into its two parts
    p1, p2 = pair.split(',')
    p1s1, p1s2 = p1.split('-')
    p2s1, p2s2 = p2.split('-')

    # check if one of the ranges fully contains the other
    if (int(p1s1) <= int(p2s1) and int(p1s2) >= int(p2s2)) or (int(p1s1) >= int(p2s1) and int(p1s2) <= int(p2s2)):
        counter_part_1 += 1
    # check if one of the ranges fully contains the other
    if (int(p1s1) <= int(p2s1) <= int(p1s2)) or \
            (int(p1s1) <= int(p2s2) <= int(p1s2)) or \
            (int(p2s1) <= int(p1s1) <= int(p2s2)) or \
            (int(p2s1) <= int(p1s2) <= int(p2s2)):
        counter_part_2 += 1

# print the result
print("Solution day 1, part 1: ", counter_part_1)
print("Solution day 1, part 1: ", counter_part_2)
