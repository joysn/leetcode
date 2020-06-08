# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

    # 2
   # / \
  # 1   3

# Input: [2,1,3]
# Output: true
# Example 2:
    # 5
   # / \
  # 1   4
     # / \
    # 3   6
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solition
class Solution:
    
    def helper(self,root,min_val,max_val):    
        if not root:
            return True
        
        if min_val is not None and root.val <= min_val:
            return False
        
        if max_val is not None and root.val >= max_val:
            return False
        
        return self.helper(root.left,min_val,root.val) and self.helper(root.right,root.val,max_val)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root,None,None)
		
# Iterative Solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre and node.val <= pre.val:
                return False
            pre, root = node, node.right
        return True
