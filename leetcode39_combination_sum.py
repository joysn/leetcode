# https://leetcode.com/problems/combination-sum/submissions/
# 39. Combination Sum
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
  # [7],
  # [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
  # [2,2,2,2],
  # [2,3,3],
  # [3,5]
# ]

class Solution:
    def sort(self, candidates):
        min_num = min(candidates)
        max_num = max(candidates)
        
        tbl = [0]*(max_num-min_num+1)
        for i in range(len(candidates)):
            tbl[candidates[i]-min_num] = candidates[i]

        j = 0
        for i in range(max_num-min_num+1):
            if tbl[i] != 0:
                candidates[j] = tbl[i]
                j += 1

    def parse(self, candidates, target, counted, right_idx, op):
        if target == 0:
            op.append(counted)
        else:
            for i in range(right_idx,-1,-1):
                if candidates[i] <= target:
                    new_counted = counted[:]
                    new_counted.append(candidates[i])
                    self.parse(candidates,target-candidates[i],new_counted,i,op)
                

    def combinationSum(self, candidates, target):
        self.sort(candidates)
        #print(candidates)
        op = []
        self.parse(candidates, target, [],len(candidates)-1,op)
        return op
        