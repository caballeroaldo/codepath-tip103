# Calculate Fabric Waste 

# In the sustainable fashion industry, minimizing waste is crucial. After cutting out patterns for clothing items, there are often leftover pieces of fabric that cannot be used.
# Your task is to calculate the total amount of fabric waste generated after producing a collection of clothing items. 
# Each clothing item requires a certain amount of fabric, and the available fabric rolls come in fixed lengths.

# Write the calculate_fabric_waste() function, which takes a list of clothing items (each with a required fabric length) 
# and a list of fabric rolls (each with a specific length). The function should return the total fabric waste after producing all the items.

# Evaluate the time and space complexity of your solution. Define your variables 
# and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
Idea is to calculate the difference at each of the items and adding them to the main counter of the waste fabric
TC: O(n)
SC: O(1)
'''
def calculate_fabric_waste(items, fabric_rolls):
    wasted_fabric = 0
    for idx, item in enumerate(items):
        diff = fabric_rolls[idx] - item[1]
        wasted_fabric += diff

    return wasted_fabric

items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls_1 = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls_2 = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls_3 = [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls_1))
print(calculate_fabric_waste(items_2, fabric_rolls_2))
print(calculate_fabric_waste(items_3, fabric_rolls_3))

'''
Example Output:
5
3
6
'''