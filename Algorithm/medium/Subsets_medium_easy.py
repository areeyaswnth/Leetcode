# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        for i in range(1<<len(nums)):
            subset = [nums[j] for j in range(0,len(nums)) if i & (1<<j)>0]
            subsets.append(subset)
        return subsets