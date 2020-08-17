# https://leetcode.com/problems/wiggle-sort-ii/
# 324. Wiggle Sort II
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# Example 1:
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].

# Example 2:
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].

# Small half:    4 . 3 . 2 . 1 . 0 .
# Large half:    . 9 . 8 . 7 . 6 . 5
# ----------------------------------
# Together:      4 9 3 8 2 7 1 6 0 5
# Just write the numbers 9, 8, 7, etc at indexes 1, 3, 5, etc. Use modulo to wrap around for the second round (the even indexes).

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        
        l = len(nums)
        for i,num in enumerate(nums[::-1]):
            #print("....",1+2*i,(l|1),(1+2*i) % (l|1))
            nums[(1+2*i) % (l|1)] = num
        