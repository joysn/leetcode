# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# 1296. Divide Array in Sets of K Consecutive Numbers

# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.
# Example 1:
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# Example 4:
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        l = len(nums)
        
        if l < k:
            return False
        
        count = collections.Counter(nums)
        #print(count)
        
        for num in nums:
            if count[num] > 0:
                
                while True:
                    if count[num-1] > 0:
                        num = num-1
                    else:
                        break
                #print("Processing ",num)
                for i in range(k):
                    #print("...Dealing with ",num+i,"  with count ",count[num+i])
                    if count[num+i] > 0:
                        count[num+i] -= 1
                    else:
                        return False
        return True
                
        