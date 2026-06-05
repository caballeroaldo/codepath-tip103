# Remove duplicates
def remove_dupes(items):
    # left and right pointer at the start of the array
    # Check if left and right pointer are the same, add to duplicate_counter
    # Iterate through until the end, return the (subtract len(items) - duplicate_counter)
    if not items:
        return 0

    duplicate_counter = 0
    left = 0
    for right in range(1,len(items)):
        if items[right] == items[left]:
            duplicate_counter += 1
        else:
            left = right

    return len(items) - duplicate_counter



items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))