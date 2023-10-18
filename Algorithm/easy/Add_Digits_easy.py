# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1
 
class Solution:
    def addDigits(self, num: int) -> int:
        sumTemp=num
        temp=num
        while(sumTemp>=10):
            sum=0
            temp=sumTemp
            while (temp>0):
                sum+=temp%10
                temp=temp//10
            sumTemp=sum
        return sumTemp