# https://leetcode.com/problems/contains-duplicate-iii/
# 220. Contains Duplicate III
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# O(n*t)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        l = len(nums)
        if l < k:
            k = l-1
            #print(k)
                
        for i in range(l-1):
            end = k+1
            #print(i+k)
            if i+k >= l:
                end = l-i
                #print("end is",end)
            for diff in range(1,end):
                #print(i,diff,nums[i],nums[i+diff])
                if abs(nums[i] - nums[i+diff]) <= t:
                    return True
                
				

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or k<1 or t<0 or (t==0 and len(nums)==len(set(nums))): return False
        for i in range(len(nums)):
            for j in range(1,k+1):
                if (i+j)>=len(nums): break
                if abs(nums[i+j]-nums[i])<=t: return True
        return False
