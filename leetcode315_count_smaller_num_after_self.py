# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 315. Count of Smaller Numbers After Self
# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# Example 1:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

class Node:
    def __init(self,val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        
class Tree:
    def __init__(self,nums):
        self.nums = nums
        self.tree = None
        if self.nums:
            self.tree = self._build(0,len(self.nums)-1)
            
            
    def _build(self,start,end):
        node = Node()
        if start == end:
            node.val = self.nums[start]
            return node
        mid = (start + end)//2
        node.left = self._build(start,mid)
        node.right = self._build(mid+1,end)
        node.val = node.left.val + node.right.val
        return node
    
    def update(self,idx, val):
        self._update(self.tree, 0, len(self.nums)-1, idx,val)
        
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.nums[idx] += val
            node.val += val
        else:
            mid = (start+end)//2
            if idx <= mid:
                self._update(node.left,start,mid,idx,val)
            else:
                self._update(node.right,mid+1,end,idx,val)
            node.val = node.left.val + node.right.val
        
        
    def query(self,i,j):
        return self._query(self.tree,0,len(self.nums)-1,i,j)
        
    def _query(self,node, start, end, l, r):
        if start > r or  end < l:
            return 0
        if l <= start and r >= end:
            return node.val
            
        mid = (start + end)//2
        q1 = self._query(node.left, start, mid, l, r)
        q2 = self._query(node.right, mid+1, end, l, r)
        return q1 + q2
            
        
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        op = []
        
        # Determine the position as per ascending order of inputs
        # I/P = [5,2,6,1],  = {1: 0, 2: 1, 5: 2, 6: 3}
        rank = {v: i for i, v in enumerate(sorted(nums))}
        
        # Create a tree with all [0,0,0,0]
        tree = Tree([0]*len(nums))
        
        # in [5,2,6,1] => [1,6,2,5]
        for i in range(len(nums)-1, -1, -1):
            # if the first element in the rank, o/p is zero, and its value is incremented by 1
            if rank[nums[i]] == 0:
                op.append(0)
                tree.update(0, 1)
            # else, get the val of the tree from [0 - curr.rank -1] and insert in o/p
            # update the tree for curr by 1
            else:
                op.append(tree.query(0, rank[nums[i]]-1))
                tree.update(rank[nums[i]], 1)
        return op[::-1]