# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
#         Input: n = 1
#         Output: true
#         Explanation: 20 = 1

# Example 2:
#         Input: n = 16
#         Output: true
#         Explanation: 24 = 16
#         Example 3:

# Input: n = 3
#         Output: false
 
# Follow up: Could you solve it without loops/recursion?

class Solution(object):
    def isPowerOfTwo(self, n):
        string=bin(n)

        print(string)
        one=string.count('1')
        zero=string.count('0')
        negative=string.count('-')
        print(one)
        if(one!=1 or negative==1): return False
        else: return True