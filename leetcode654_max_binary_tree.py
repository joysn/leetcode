# https://leetcode.com/problems/maximum-binary-tree/
# 654. Maximum Binary Tree
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
      # 6
    # /   \
   # 3     5
    # \    / 
     # 2  0   
       # \
        # 1
		
		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        l = len(nums)

        pos_dict = {}
        for idx in range(l):
            pos_dict[nums[idx]] = idx
        
        nums.sort(reverse=True)
        #print(nums)
        root = None
        for e in nums:
            n = TreeNode(e)
            if root is None:
                root = n
            else:
                temp = root
                while True:
                    if pos_dict[e] > pos_dict[temp.val]:
                        if temp.right is None:
                            temp.right = n
                            break
                        else:
                            temp = temp.right
                    else:
                        if temp.left is None:
                            temp.left = n
                            break
                        else:
                            temp = temp.left
                            
        return root

        
            