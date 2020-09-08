# https://leetcode.com/problems/partition-equal-subset-sum/
# 416. Partition Equal Subset Sum
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution:  
    def canPartition(self, nums: List[int]) -> bool:
        
        tot = sum(nums)
        
        if tot%2 != 0:
            return False
        
        nums.sort()
        d = {}
        def find(t,csum,arr):
            if csum in d:
                return d[csum]
            if csum == t:
                return True
            if csum > t:
                return False
            for idx in range(len(arr)):
                if csum + arr[idx] > target:
                    break
                if find(t, csum + arr[idx],arr[idx+1:]):
                    d[csum] = True
                    return True
                
            d[csum] = False
            return False
    
        target = tot // 2
        return find(target,0,nums) 
                
            
        