# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

 

# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        ls=[]
        for i in s:
            if i =="(":ls.append(i)
            elif len(ls)!=0 and ls[-1]=="(" and  i==")":ls.pop()
            else:count+=1
        return len(ls)+count