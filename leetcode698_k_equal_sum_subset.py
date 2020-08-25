# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# 698. Partition to K Equal Sum Subsets
# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 
 
class Solution: 
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        
        l = len(nums)
        tot = sum(nums)
        if l < k or tot%k != 0:
            return False
        sub_sum = tot/k
        if any(num > sub_sum for num in nums):
            return False
        
        nums.sort()
        return self.dfs(sub_sum,nums[-1],nums[:-1])
        
    def dfs(self,sub_sum,cur_sum,nums):
        if cur_sum == sub_sum:
            if not nums:
                return True
            return self.dfs(sub_sum, nums[-1], nums[: -1])

        for idx in range(len(nums)):
            tmp = nums[idx]
            if nums[idx] + cur_sum <= sub_sum:
                del nums[idx]
                if self.dfs(sub_sum, cur_sum + tmp, nums):
                    return True
                nums.insert(idx,tmp)
            
        
        
        