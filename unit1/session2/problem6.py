# Merge Intervals

# You are given an array of intervals, where each interval is represented as [start, end].
# Write a function merge_intervals(intervals) that merges all overlapping intervals 
# and returns a new array of the merged, non-overlapping intervals.

def merge_intervals(intervals):
    if not intervals:
        return []
    
    sorted_intervals = sorted(intervals)
    merged = []
    current = sorted_intervals[0]

    for i in range(1, len(sorted_intervals)):
        # Check if the current[end] overlaps with next interval[start]
        if current[1] >= sorted_intervals[i][0]:
            current[1] = max(current[1], sorted_intervals[i][1])
        # If no overlap, add interval to merge and update current
        else:
            merged.append(current)
            current = sorted_intervals[i]
    
    merged.append(current)
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [2 , 5]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5], [3, 8]]
print(merge_intervals(intervals))