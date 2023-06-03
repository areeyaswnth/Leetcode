# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

    # Example 1:
        # Input: num1 = "11", num2 = "123"
        # Output: "134"
    # Example 2:
        # Input: num1 = "456", num2 = "77"
        # Output: "533"
    # Example 3:
        # Input: num1 = "0", num2 = "0"
        # Output: "0"
    
# Constraints:
    # 1 <= num1.length, num2.length <= 104
    # num1 and num2 consist of only digits.
    # num1 and num2 don't have any leading zeros except for the zero itself.

class Solution(object):
    def addStrings(self, num1, num2):
        if(len(num1)>len(num2)):
            num1,num2=num2,num1
        carry=0
        num3=""
        for i in range(1,len(num2)+1):
                if(i<=len(num1)):
                    n=int(num1[-i])+int(num2[-i])
                else:
                    n=+int(num2[-i])
                if(carry!=0): 
                    n=n+carry
                    carry=0
                if(n>=10):
                    n=n%10
                    carry=1 
                num3=str(n)+num3
        if carry==1: num3=str(carry)+num3
        return num3
            