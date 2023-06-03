#     Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
    # Example 1:
        # Input: n = 16
        # Output: true
    # Example 2:
        # Input: n = 5
        # Output: false
    # Example 3:
        # Input: n = 1
        # Output: true
# Constraints:
    # -231 <= n <= 231 - 1
class Solution(object):
    def isPowerOfFour(self, n):
        string=bin(n)

        print(string)
        one=string.count('1')
        zero=string.count('0')
        negative=string.count('-')
        print(one)
        if(one!=1 or (zero%2==0 and negative==0) or(negative==1)): return False
        else: return True