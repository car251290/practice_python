# the problem is to count the 
#number of deletions needed to 
# make a string alternating
# for example: AABAAB -> ABAB, so the answer is 2

def alternatingCharacters(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count
     