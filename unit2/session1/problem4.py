# Booby Trap

# Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. 
# The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. 
# A balanced code is one where the frequency of every letter present in the code is equal. 
# To disable the trap, Captain Feathersword must remove exactly one letter from the message. 
# Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.
# Given a 0-indexed string code consisting of only lowercase English letters, 
# write a function can_make_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal,
# and False otherwise.

from collections import Counter

def can_make_balanced(code):

    freq_map = Counter(code)
    freq_set = set(freq_map.values())

    if len(freq_set) == 1:
        return True
    
    if len(freq_set) == 2:
        a, b = sorted(freq_set)
        if a == b - 1:
            higher_freq = b
            if list(freq_map.values()).count(higher_freq) == 1:
                return True

    return False
    

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 