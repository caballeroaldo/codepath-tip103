# Find All Duplicate Treasure Checks in an Array

# Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] 
# and each integer appears once or twice. Return an array of all the integers that appear twice, 
# representing the treasure chests that have duplicates.

from collections import Counter

def find_duplicate_chests(chests):
    freq_map = Counter(chests)
    duplicate_list = []

    # for key, value in enumerate(chests):
    for key, value in enumerate(freq_map):
        if freq_map[key] == 2:
            duplicate_list.append(key)
    
    return duplicate_list
        
    


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))