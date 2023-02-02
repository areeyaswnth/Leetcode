# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        sqr=0
        while(i*i<=x):
            if i>x:
                return sqr
            sqr=i
            i+=1
        return sqr