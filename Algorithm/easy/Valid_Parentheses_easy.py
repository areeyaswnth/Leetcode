# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        myStack=[]
        open='([{'
        close=-1
        if len(s)>0 and len(s)%2==0:
            print(1)
            for i in s:
                if i in open:
                    myStack.append(i)
                elif len(myStack)!=0:
                    if i ==')':close=0
                    if i==']':close=1
                    if i=='}':close=2
                    if open[close]!=myStack[-1]: return False
                    else: myStack.pop()
                else: return False
            if len(myStack)!=0: return False
            return True
