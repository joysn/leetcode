# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# 632. Smallest Range Covering Elements from K Lists
# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
# Example 1:
# Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        v = []
        seen = set()
        l = len(nums)
        
        for idx in range(l):
            for ele in nums[idx]:
                if (ele,idx) not in seen:
                    v.append((ele,idx))
                    seen.add((ele,idx))
        v.sort()
        slow = 0
        groups = 0
        counts = collections.Counter()
        
        minR = float('inf')
        res = [0,0]
        for fast in range(len(v)):
            if counts[v[fast][1]] == 0:
                groups += 1
            counts[v[fast][1]] += 1
            while slow <= fast and groups == l:
                diff = v[fast][0] - v[slow][0]
                if diff < minR :
                    minR = diff
                    res = [v[slow][0],v[fast][0]]
                counts[v[slow][1]] -= 1
                if counts[v[slow][1]] == 0:
                    groups -= 1
                slow += 1

        return res
