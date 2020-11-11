# https://leetcode.com/problems/combinations/
# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# You may return the answer in any order.
# Example 1:
# Input: n = 4, k = 2
# Output:
# [
  # [2,4],
  # [3,4],
  # [2,3],
  # [1,2],
  # [1,3],
  # [1,4],
# ]
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]

class Solution:
    
    def parse(self, n, target, counted, left_idx, op):
        if target == 0:
            op.append(counted)
        else:
            for i in range(left_idx,n+1):
                new_counted = counted[:]
                new_counted.append(i)
                self.parse(n,target-1,new_counted,i+1,op)
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        op = []
        self.parse(n,k,[],1,op)
        return op
        