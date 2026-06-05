# Sort Array by Parity

# Given an integer array nums, write a function sort_by_parity() 
# that moves all the even integers to the beginning of the array, followed by all the odd integers.

# Return any array that satisfies this condition.

# Plan to have a pointer to the end of the even list in the beginning 
# Two pointer approach, left pointer points to the even list,
# right pointer actually iterates through the array
def sort_by_parity(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] % 2 == 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
        
        
        right += 1

    return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))