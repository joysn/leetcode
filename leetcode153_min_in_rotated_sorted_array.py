https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 153. Find Minimum in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.
# Example 1:
# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

# Linear search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l == 1:
            return  nums[0]
        
        for i in range(1,l):
            if nums[i-1] > nums[i]:
                return nums[i]
            
        if nums[0] < nums[1]:
            return nums[0]

# Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l == 1:
            return  nums[0]
        
        # No rotation
        if nums[-1] > nums[0]:
            return nums[0]
        
        left = 0
        right = l - 1
        
        while right >= left:  
            mid = left + (right-left) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        