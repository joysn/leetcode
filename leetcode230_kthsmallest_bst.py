# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
   # 3
  # / \
 # 1   4
  # \
   # 2
# Output: 1
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
       # 5
      # / \
     # 3   6
    # / \
   # 2   4
  # /
 # 1
# Output: 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
	def kthSmallest_helper(self,root: TreeNode):

	op = []

	if root is None:
		return
	
	if root.left is not None:
		op += self.kthSmallest_helper(root.left)
	op.append(root.val)
	if root.right is not None:
		op += self.kthSmallest_helper(root.right)

	return op
    
	def kthSmallest(self, root: TreeNode, k: int) -> int:

		sorted_tree = self.kthSmallest_helper(root)
		return sorted_tree[k-1]
		
		
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#  Solution 2
class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		stack = []
		curr = root
		while True:
		
			while curr is not None:
				stack.append(curr)
				curr = curr.left

			if len(stack) == 0:
				break
                
			curr = stack.pop()
			k -= 1
			if k == 0:
				return curr.val
			
			curr = curr.right