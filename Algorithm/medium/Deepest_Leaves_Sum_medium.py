# Given the root of a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:


# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_level=0
    sum=0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.traveltree(root,0)
        return (self.sum)
    def traveltree(self,root,level):
        if root:
            if level>self.max_level:
                self.max_level=level 
                self.sum=root.val
            elif level==self.max_level:
                self.sum+=root.val
            self.traveltree(root.left,level+1)
            self.traveltree(root.right,level+1)
        else: 
            return None