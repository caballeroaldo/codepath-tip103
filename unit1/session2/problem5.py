# Container with Most Honey

# Christopher Robin is helping Pooh construct the biggest hunny jar possible.
# Help him write a function that accepts an integer array heights of length n. 
# The height of each element is given by heights[i].
# There are n vertical lines drawn such that 
# the two endpoints of the ith line are (i, 0) and (i, heights[i]).
# Find two lines that, together with the x-axis, 
# form the container that holds the most honey.
# Return the maximum amount of honey a container can store.

def most_honey(heights):
    max_honey = float('-inf')

    left = 0
    right = len(heights) - 1
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        local_honey = height * width
        max_honey = max(max_honey, local_honey)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_honey

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))