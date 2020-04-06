# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
# Given a binary tree, return the inorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
   # 1
    # \
     # 2
    # /
   # 3
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
        
		if root is None:
			return
        
		# op = []
		# if root.left is not None:
		#     op += self.inorderTraversal(root.left)
		# op.append(root.val)
		# if root.right is not None:
		#     op += self.inorderTraversal(root.right)

		stack = []
		op = []
		curr = root
		while True:
			while curr is not None:
				stack.append(curr)
				curr = curr.left
			if len(stack) == 0:
				break
			curr = stack.pop()
			op.append(curr.val)
			curr = curr.right
        print(op)
        return op
        