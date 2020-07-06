# https://leetcode.com/problems/path-sum-ii/
# 113. Path Sum II
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
      # 5
     # / \
    # 4   8
   # /   / \
  # 11  13  4
 # /  \    / \
# 7    2  5   1
# Return:
# [
   # [5,4,11,2],
   # [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def helper(path,root,target):
            
            if not root:
                return
            
            if root.left is None and root.right is None:
                if target == root.val:
                    res.append(path+[root.val])
                    
            else:
                helper(path+[root.val],root.left,target-root.val)
                helper(path+[root.val],root.right,target-root.val)
        
        res = []
        helper([],root,sum)
        return res
            
        