# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        l = len(nums)
        
        tot_dict = dict()
        tot_dict[0] = 1
        tot = 0
        for i in range(l):
            tot += nums[i]
            if tot-k in tot_dict:
                cnt += tot_dict[tot-k]
            if tot in tot_dict:
                tot_dict[tot] += 1
            else:
                tot_dict[tot] = 1
            
        
        return cnt
        