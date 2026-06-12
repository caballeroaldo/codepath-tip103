# Gallery Wall 

# You are tasked with organizing a collection of art prints represented by a list of strings collection. 
# You need to display these prints on a single wall in a 2D array format that meets the following criteria:
#     The 2D array should contain only the elements of the array collection.
#     Each row in the 2D array should contain distinct strings.
#     The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them. 
# Note that the 2D array can have a different number of elements on each row.

from collections import Counter

def organize_exhibition(collection):
    artist_count = Counter(collection)

    result = []

    while artist_count:
        current_row = []

        for artist in list(artist_count.keys()):
            current_row.append(artist)
            artist_count[artist] -= 1

            if artist_count[artist] == 0:
                del artist_count[artist]
        
        result.append(current_row)

    return result

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))