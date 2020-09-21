# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array
# Given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You should search for target in nums and if you found return its index, otherwise return -1.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = len(nums)
        
        if l == 0:
            return -1
        if l == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if l == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
            
        low = 0
        hi = l-1
        
        while (low <= hi):
            m = low + (hi - low)//2
            #print(low,m,hi,nums[m])
            if target == nums[m]:
                return m
            if m == low or m == hi:
                #print("We should be here")
                if nums[low] == target:
                    return low
                elif nums[hi] == target:
                    return hi
                else:
                    return -1
                
            if nums[low] < nums[m] and nums[m] < nums[hi]:
                # no pivot
                if target < nums[m]:
                    hi = m-1
                else:
                    low = m+1
            elif nums[low] < nums[m] and nums[m] > nums[hi]:
                # pivot on right side, left is okay
                if target < nums[m] and target >= nums[low]:
                    # on the left side
                    hi = m-1
                else:
                    # on the right side
                    low = m+1
            else:
                #print("In else")
                # pivot on left and right is okay
                if target > nums[m] and target <= nums[hi]:
                    # on right side
                    low = m+1
                else:
                    hi = m-1
        return -1
                
        
        