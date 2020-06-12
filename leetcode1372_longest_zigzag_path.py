# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/submissions/
# 1372. Longest ZigZag Path in a Binary Tree
# Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right then move to the right child of the current node otherwise move to the left child.
# Change the direction from right to left or right to left.
# Repeat the second and third step until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.
# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:
# Input: root = [1]
# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        
        res = 0
        q = deque([(root,0,0)])
        
        
        while q:
            node,left,right = q.popleft()
            res = max(res,left,right)
            
            if node.left is not None:
                q.append((node.left,0,left+1))
            if node.right is not None:
                q.append((node.right,right+1,0))

        return res



## Recursive Method
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.maxSize = 0
        
    def longestZigZag(self, root: TreeNode) -> int:
        
        debug = False
        
        def countNode(root,count,left):
            
            if root is None:
                return count
            
            count += 1
            if self.maxSize < count:
                self.maxSize = count
                
            print("MaxSize",self.maxSize,"count",count,"left",left) if debug else None
            if left == 1 and root.left is not None:
                print("Going left") if debug else None
                countNode(root.left,count,0)
            elif left == 0 and root.right is not None:
                print("Going right",root.right.val) if debug else None
                countNode(root.right,count,1)
            if root.right is not None:
                print("Going right",root.right.val) if debug else None
                countNode(root.right,0,1)
            if root.left is not None:
                print("Going left") if debug else None
                countNode(root.left,0,0)
                
            print("Done") if debug else None
            
            
        if root is None:
            return 0
        
        if root.left is not None:
            print("MaxSize",self.maxSize,"count",0,"left",1) if debug else None
            print("Going left") if debug else None
            countNode(root.left,0,0)
        if root.right is not None:
            print("MaxSize",self.maxSize,"count",0,"left",0) if debug else None
            print("Going right") if debug else None
            countNode(root.right,0,1)
            
        return self.maxSize