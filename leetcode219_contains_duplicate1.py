# https://leetcode.com/problems/contains-duplicate-ii/submissions/
# 219. Contains Duplicate II
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = len(nums)
        if not nums or k<1 or (l == len(set(nums))):
            return False
        
        for i in range(l):
            for j in range(i+1,i+k+1):
                if j >= l:
                    break
                if nums[i] == nums[j]:
                    return True
        