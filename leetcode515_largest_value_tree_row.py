# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# 515. Find Largest Value in Each Tree Row
# You need to find the largest value in each row of a binary tree.
# Example:
# Input: 

          # 1
         # / \
        # 3   2
       # / \   \  
      # 5   3   9 

# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        if root:
            op = [root.val]
        else:
            return []
        
        nodes = [root]
        while True:
            temp_nodes = []
            mx = -math.inf
            while len(nodes) > 0:
                n = nodes.pop()
                if n.left:
                    temp_nodes.append(n.left)
                    if mx < n.left.val:
                        mx = n.left.val
                if n.right:
                    temp_nodes.append(n.right)
                    if mx < n.right.val:
                        mx = n.right.val
            if len(temp_nodes) > 0:
                nodes = temp_nodes
                op.append(mx)
            else:
                break
        
        return op
                
        