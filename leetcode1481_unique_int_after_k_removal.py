# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# 1481. Least Number of Unique Integers after K Removals
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Example 1:
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        l = len(arr)
        if l == 0:
            return 0
        if k > len(arr):
            return None
        
        sl = sorted(collections.Counter(arr).items(), key = lambda kv:(kv[1],kv[0]))
        c = 0
        while c < k:
            c += sl[0][1]
            if c <= k:
                sl.pop(0)
        
        return len(sl)
            
        
        
        