# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
 

# Example 1:

# Input: nums1 = [4,1,3], nums2 = [5,7]
# Output: 15
# Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
# Example 2:

# Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
# Output: 3
# Explanation: The number 3 contains the digit 3 which exists in both arrays.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 9
# 1 <= nums1[i], nums2[i] <= 9
# All digits in each array are unique.
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ls=list(set(nums1).intersection(set(nums2)))
        if len(ls)>1:
            return min(ls)
        elif len(ls)==1:return ls[0]
        else:
            nums1.sort()
            nums2.sort()
            if nums1[0]>nums2[0]:return (nums2[0]*10)+nums1[0]
            else:return (nums1[0]*10)+nums2[0]