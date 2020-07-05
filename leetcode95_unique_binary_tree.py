# https://leetcode.com/problems/unique-binary-search-trees-ii/
# 95. Unique Binary Search Trees II
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
# Example:
# Input: 3
# Output:
# [
  # [1,null,3,2],
  # [3,2,null,1],
  # [3,1,null,null,2],
  # [2,1,3],
  # [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

   # 1         3     3      2      1
    # \       /     /      / \      \
     # 3     2     1      1   3      2
    # /     /       \                 \
   # 2     1         2                 3
# Constraints:
# 0 <= n <= 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self,start, end):

        if start > end:
            return [None]
        
        if start == end:
            return [TreeNode(start)]
        
        if self.cache[start][end]:
            return self.cache[start][end]
        
        for root in range(start,end+1):
            left = self.helper(start,root-1)
            right = self.helper(root+1,end)
            for lt in left:
                for rt in right:
                    x = TreeNode(root)
                    x.left = lt
                    x.right = rt
                    self.cache[start][end].append(x)
        return self.cache[start][end]
        
        
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        self.cache = [[[] for i in range(n+1)] for j in range(n+1)]
        return self.helper(1,n)
        
        