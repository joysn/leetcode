# https://leetcode.com/problems/combination-sum-iv/
# 377. Combination Sum IV
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# Example:
# nums = [1, 2, 3]
# target = 4
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

# Note that different sequences are counted as different combinations.
# Therefore the output is 7.

# REcursion
class Solution:
    def dfs(self,nums,target,path,res):
        if target == 0:
            res.append(path)
        else:   
            for i in range(len(nums)):
                if nums[i] <= target:
                    t_path = path[:]
                    t_path.append(nums[i])
                    #print(t_path)
                    self.dfs(nums,target-nums[i],path+[nums[i]],res)
        
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res,path,idx = [],[],0
        self.dfs(nums,target,path,res)
        return len(res)
    
	
	
# Top down with memoization
class Solution:         
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def recCount(startIdx, nums, target, mem):
            
            if target == 0:
                return 1
            if target < 0:
                return 0
            if (startIdx,target) in mem:
                return mem[(startIdx,target)]
            
            mem[(startIdx,target)] = 0
            # circle the nums array starting from the given startIdx
            # not exclude the current num pointed by the startIdx for the next recursion
            for i in range(startIdx, startIdx + len(nums)):
                mem[(startIdx,target)] += recCount(i % len(nums) , nums, target - nums[i % len(nums)], mem)
                
            return mem[(startIdx,target)]
        
        # memorize each pair of starting Idx and target
        mem = {}
        return recCount(0,nums,target,mem)
		
# Bottom up
class Solution:         
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums, combs = sorted(nums), [1] + [0] * (target)
        
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]
    