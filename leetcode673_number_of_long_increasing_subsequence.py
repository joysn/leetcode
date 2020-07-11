# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# 673. Number of Longest Increasing Subsequence
# Given an unsorted array of integers, find the number of longest increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l <= 1:
            return l

        mxsize = 1
        mxsize_cnt = 1
        
        cache = [[1,1] for c in range(l)]
        for end in range(1,l):
            for prev in range(end):
                if nums[end]  > nums[prev]:
                    cur_len, cur_count = cache[prev][0]+1, cache[prev][1]
                    if cur_len > cache[end][0]:
                        cache[end] = [cur_len,cur_count]
                    elif cur_len == cache[end][0]:
                        cache[end][1] += cur_count
            
            if cache[end][0] > mxsize:
                mxsize, mxsize_cnt = cache[end][0], cache[end][1]
            elif cache[end][0] == mxsize:
                mxsize_cnt += cache[end][1]
                
        return mxsize_cnt
                
                        
    
        