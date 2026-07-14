# Find Most Frequent Keywords
 
# Identify the most frequently used keywords from a dictionary where the keys are scene names and the values are lists of keywords used in each scene. Return the keyword that appears the most frequently across all scenes. If there is a tie, return all the keywords with the highest frequency.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_most_frequent_keywords(scenes):
  pass

scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) 

'''
Example Output:
['action', 'hero']
['love', 'drama']
'''