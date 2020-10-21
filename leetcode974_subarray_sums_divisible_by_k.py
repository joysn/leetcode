# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# 974. Subarray Sums Divisible by K
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
# Example 1:
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        cnt = 0
        l = len(A)
        
        mod_dict = dict()
        mod_dict[0] = 1
        tot = 0
        for i in range(l):
            tot += A[i]
            mod = tot%K
            if mod in mod_dict:
                cnt += mod_dict[mod]
            if mod in mod_dict:
                mod_dict[mod] += 1
            else:
                mod_dict[mod] = 1
                
        return cnt
        