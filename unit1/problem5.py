# Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. 
# Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. 
# The function accepts two integers lower and upper and a unique integer array clues. 
# All elements in clues are within the inclusive range [lower, upper].
# A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
# That is, no element of clues is included in any of the ranges, 
# and each missing number is covered by one of the ranges.

def find_missing_clues(clues, lower, upper):
    clues = sorted(clues)
    missing_ranges = []

    # if no clues, the whole range is missing
    if not clues:
        if lower <= upper:
            return [[lower, upper]]
        return []

    # missing before the first clue
    if lower < clues[0]:
        missing_ranges.append([lower, clues[0] - 1])

    # missing between clues
    for i in range(len(clues) - 1):
        current = clues[i]
        next_val = clues[i + 1]
        if next_val - current > 1:
            missing_ranges.append([current + 1, next_val - 1])

    # missing after the last clue
    if clues[-1] < upper:
        missing_ranges.append([clues[-1] + 1, upper])

    return missing_ranges



clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))