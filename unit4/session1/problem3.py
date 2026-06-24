# Fashion Trends

# In the fast-changing world of fashion, certain materials and practices become trending based on how frequently they are adopted by brands. 
# You want to identify which materials and practices are trending.
# A material or practice is considered "trending" if it appears in the dataset more than once.

# Write the find_trending_materials() function, which takes a list of brands (each with a list of materials or practices)
# and returns a list of materials or practices that are trending (i.e., those that appear more than once across all brands).

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
# for why you believe your solution has the stated time and space complexity.

'''
Idea is to go through the dictionary and count the amount of times materials appear to determine if they are trending

Go through the dictionary, have a set iterate through, if the material is in the set, add to a list and return the list

TC: O(n*m) - n is the size of the list of brands and m is the size of the materials list in each brand
SC: O(m) - m is the size of the list of materials in each brand
'''
def find_trending_materials(brands):
    trending_materials = []
    material_set = set()

    for brand in brands:
        for material in brand["materials"]:
            if material in material_set:
                trending_materials.append(material) 
            else:
                material_set.add(material)

    return trending_materials

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

'''
Expected Output:
['organic cotton', 'recycled polyester', 'bamboo']
['hemp', 'linen']
['recycled polyester']
'''