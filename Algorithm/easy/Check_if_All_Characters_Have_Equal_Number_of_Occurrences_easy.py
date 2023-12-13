# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s=list(s)
        s.sort()
        lst=[]
        flag=s[0]
        count=0
        for i in s:
            if i!=flag:
                lst.append(count)
                flag=i
                count=0
            if len(set(lst))!=1 and len(lst)!=0: return False
            count+=1
        lst.append(count)
        return len(set(lst))==1
        
 