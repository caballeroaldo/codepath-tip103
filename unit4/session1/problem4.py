# Fabric Pairing

# You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. 
# Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics 
# whose combined cost is the highest possible without exceeding the budget.

# Write the find_best_fabric_pair() function, which takes a list of fabrics (each with a name and cost) and a budget. 
# The function should return the names of the two fabrics whose combined cost is the closest to the budget without exceeding it.

# Evaluate the time and space complexity of your solution. Define your variables and 
# provide a rationale for why you believe your solution has the stated time and space complexity.

'''
Idea is to iterate through the list and determine the cost closest to the budget without going over.
- Consider taking the smallest difference between the budget and the cost 
- Also consider sorting the list by cost in ascending order and applying two pointer 
TC: O(nlogn) -- Due to the sorting, it will take the most time during the run of the algorithm
SP: O(1)
'''

def find_best_fabric_pair(fabrics, budget):
    fabrics.sort(key = lambda x: x[1]) # lambda function to sort fabrics by cost
    left = 0 
    right = len(fabrics) - 1

    best_pair = ()
    closest_sum = 0

    while left < right:
        cost_sum = fabrics[left][1] + fabrics[right][1]

        if cost_sum > closest_sum and cost_sum <= budget:
            closest_sum = cost_sum
            best_pair = (fabrics[left][0], fabrics[right][0])
        elif cost_sum > budget:
            right -= 1
        else:
            left += 1

    return best_pair

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

'''
Expected Output:
('Hemp', 'Organic Cotton')
('Tencel', 'Recycled Wool')
('Bamboo', 'Linen')
'''