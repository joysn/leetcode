# https://leetcode.com/problems/continuous-subarray-sum/submissions/
# 523. Continuous Subarray Sum
# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42

# Approach 1
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        l = len(nums)
        
        if l == 0 or l == 1:
            return False
        
        if k < 0:
            k *= -1
        
        if k == 1:
            return True
            
        cache = [[0 for c in range(l)] for r in range(l)]
        
        for r in range(l):
            cache[r][r] = nums[r]
        
        for r in range(l):
            for c in range(r+1,l):
                cache[r][c] = cache[r][c-1] + nums[c]
                #print(r,c,cache[r][c])
                
                if cache[r][c] == 0:
                    return True
                if k != 0:
                    if cache[r][c] % k == 0:
                        return True
        #print(cache)
        return False
                

# Approach 2
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        l = len(nums)
        
        if l == 0 or l == 1:
            return False
        
        if k < 0:
            k *= -1
        
        if k == 1:
            return True
        
        if k != 0:
            for i in range(l):
                nums[i] %= k
            
        cache = [[0 for c in range(l)] for r in range(l)]
        
        for r in range(l):
            cache[r][r] = nums[r]
        
        for r in range(l):
            for c in range(r+1,l):
                cache[r][c] = cache[r][c-1] + nums[c]
                #print(r,c,cache[r][c])
                
                if cache[r][c] == 0:
                    return True
                if k != 0:
                    if cache[r][c] < k:
                        continue
                    elif cache[r][c] == k:
                        return True
                    else:
                        cache[r][c] -= k
        #print(cache)
        return False
  
# O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        l = len(nums)
        
        if l == 0 or l == 1:
            return False
        if k < 0:
            k *= -1
        if k == 1:
            return True
        
        if k == 0:
            for i in range(1,l):
                if nums[i-1] + nums[i] == 0:
                    return True
            return False
        
        rem = {}
        csum = 0
        for i in range(l):
            csum += nums[i]
            crem = csum%k    
            if crem == 0 and i != 0:
                return True
            elif crem in rem:
                if i - rem[crem] > 1:
                    return True
            else:
                rem[crem] = i
        
        
        return False
                
        