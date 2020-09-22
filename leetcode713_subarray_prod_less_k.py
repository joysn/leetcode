# https://leetcode.com/problems/subarray-product-less-than-k/
# 713. Subarray Product Less Than K
# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = len(nums)
        if l <= 0:
            return 0
        
        status = (1,0)
        result = 0
        for i, num in enumerate(nums):
            product,left = status
            product *= num
            while product >= k and left < i+1:
                product /= nums[left]
                left += 1
            status = (product,left)
            result += i -(left-1)
            
        return result
            
                    
                    
                
                