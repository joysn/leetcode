# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
   # 1
    # \
     # 2
    # /
   # 3
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		if root is None:
			return
		op = []
		if root.left is not None:
			op += self.postorderTraversal(root.left)
		if root.right is not None:
			op += self.postorderTraversal(root.right)
		op.append(root.val)
		return op


class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		if root is None:
			return
		op = []
		stack = []
		curr = root
		
		while True:
			 while curr is not None:
				stack.append((curr,0))
				curr = curr.left
			if len(stack) == 0:
				break
				
			curr,flag = stack.pop()
			if flag == 0:
				stack.append((curr,1))
				curr = curr.right
			else:
				op.append(curr.val)
				curr = None
		return op

