# Fabric Roll Organizer

# You need to organize fabric rolls for optimal usage. Each fabric roll has a specific length, 
# and you want to sort the rolls by length and pair adjacent rolls together. 
# If there's an odd number of rolls, one roll will be left out.

# Write the organize_fabric_rolls() function, which takes a list of fabric roll lengths, sorts them, 
# and returns a list of pairs of adjacent fabric roll lengths. If there's an odd number of rolls, the last (largest) roll should be returned separately.

# Evaluate the time and space complexity of your solution. Define your variables 
# and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
Function should sort the fabric rolls in ascending order, should be grouped in pairs, but if odd, the last number should be by itself
Returns a list of these tuples and single roll (if it's an odd number)
TC: O(nlogn)
SC: O(n)
'''
def organize_fabric_rolls(fabric_rolls):
    result = []

    fabric_rolls.sort()
    
    i = 0
    while i < len(fabric_rolls) - 1:
        result.append((fabric_rolls[i], fabric_rolls[i+1]))
        i += 2
    
    if len(fabric_rolls) % 2 == 1:
        result.append(fabric_rolls[len(fabric_rolls) - 1])

    return result

fabric_rolls = [15, 10, 25, 30, 22]
fabric_rolls_2 = [5, 8, 10, 7, 12, 14]
fabric_rolls_3 = [40, 10, 25, 15, 30]

print(organize_fabric_rolls(fabric_rolls))
print(organize_fabric_rolls(fabric_rolls_2))
print(organize_fabric_rolls(fabric_rolls_3))

'''
Example Output:
[(10, 15), (22, 25), 30]
[(5, 7), (8, 10), (12, 14)]
[(10, 15), (25, 30), 40]
'''