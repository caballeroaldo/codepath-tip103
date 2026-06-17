# Reveal Attendee List in Order

# You are planning a special event where each attendee has a unique registration number. 
# These numbers are listed in the provided array attendees, but they are currently out of order.

# At the event, attendees will walk on stage one by one following this special reveal process:
#    1. The person at the front of the line walks on stage (this number is revealed).
#    2. If there are still people left in line, the next person in front moves to the back of the line.
#    3. Steps 1 and 2 repeat until everyone has walked on stage.

# Your task is to rearrange the attendees list before the process starts so that the attendees walk 
# on stage by registration number in increasing order.

# Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, 
# such that when the attendees follow the above reveal process they walk on stage from smallest 
# registration number to largest registration number.

''' UMPIRE template 

# Understand 
    inputs: array of attendees not in order
    outputs: array of attendees with the correct order
    constraints: 
    edge cases:

# Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of)

# Plan (pseudocode) 
  
# Implement (python code)

# Review (dry run of your code)

# Evaluate (time and space complexity)
'''

from collections import deque 

def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    # Queue to keep track of the indices
    index_queue = deque(range(n))
    result = [0] * n

    # iterate through the attendees when it's sorted
    for attendee in sorted(attendees):
        result[index_queue.popleft()] = attendee # add to result from the queue into the result to do step 1 in the problem statement
        if index_queue: # when the queue is not empty move the next index to the back to do step 2 in the problem statement
            index_queue.append(index_queue.popleft())

    return result

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  

# Example Output:
# [2,13,3,11,5,17,7]
# [1,1000]