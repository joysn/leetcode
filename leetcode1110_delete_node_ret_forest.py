# https://leetcode.com/problems/delete-nodes-and-return-forest/
# 1110. Delete Nodes And Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result in any order.

# Example 1:
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# [1,2,null,4,3]
# [2,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        
        op = [root]
        stack = [root]
        
        while len(stack) > 0:
            troot = stack.pop()
            #print(troot.val)
            if troot.right:
                stack.append(troot.right)
                if troot.right.val in to_delete:
                    troot.right = None
            if troot.left:
                stack.append(troot.left)
                if troot.left.val in to_delete:
                    troot.left = None
            if troot.val in to_delete:
                if troot in op:
                    op.remove(troot)
                if troot.left:
                    op.append(troot.left)
                if troot.right:
                    op.append(troot.right)
            if not to_delete:
                break
        return op
