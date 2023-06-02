# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
class Solution(object):
    def addBinary(self, a, b):
        print(self.strtobinary(b))
        sum=self.strtobinary(a)+self.strtobinary(b)
        return format(sum, "b")
    def strtobinary(self,a):
        sum=0
        for i in range(0,len(a)):
            sum=2**i *int(a[-i-1])+sum
        return sum