# https://leetcode.com/problems/combination-sum-ii/
# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
  # [1, 7],
  # [1, 2, 5],
  # [2, 6],
  # [1, 1, 6]
# ]
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
  # [1,2,2],
  # [5]
# ]

class Solution:
    
    def parse(self,candidates,target,counted,left_idx,op):
        if target == 0:
            op.add(tuple(counted))
        else:
            for i in range(left_idx,len(candidates)):
                if candidates[i] <= target:
                    new_counted = counted[:]
                    new_counted.append(candidates[i])
                    self.parse(candidates,target-candidates[i],new_counted,i+1,op)
        
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        op = set()
        self.parse(candidates,target,[],0,op)
        return op
        
                
                
            
        