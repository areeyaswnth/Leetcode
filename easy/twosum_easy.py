class Solution(object):
    def __init__(self,target) :
        self.target=target
    def twoSum(self, nums):
        return self.target+nums

inp = input().split()
ans=Solution(inp[0])
print(ans.twoSum(inp[1]))