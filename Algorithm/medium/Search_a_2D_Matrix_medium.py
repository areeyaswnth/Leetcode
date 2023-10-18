# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
# Accepted
# 1.5M
# Submissions
# 3.1M
# Acceptance Rate
# 49.3%
class Solution(object):
    def binarySearch(self,arr,l,r,target):
        m=(l+r)/2
        print(arr[m])
        if (r>=l):
            if arr[m]==target:
                print(arr[m])
                return True
            elif arr[m]>target:
                return self.binarySearch(arr,l,m-1,target)
            elif arr[m]<target:
                return self.binarySearch(arr,m+1,r,target)
            else: return False
        else:
            
            return False
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            if (self.binarySearch(matrix[i],0,n-1,target)):
               
                return True
        return False