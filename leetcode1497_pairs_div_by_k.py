# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/submissions/
# 1497. Check If Array Pairs Are Divisible by k

# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return True If you can find a way to do that or False otherwise.

# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
# Example 4:
# Input: arr = [-10,10], k = 2
# Output: true
# Example 5:
# Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# Output: true

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        
        l = len(arr)
        print(l)
        if l % 2 != 0:
            return False
        
        
        tot = sum(arr)
        
        if tot%k != 0:
            return False
        
        
        lookup = collections.defaultdict(int)
        cnt = 0
        for idx in range(l):
            key = k - arr[idx]%k
            if key in lookup and lookup[key] > 0:
                cnt += 1
                lookup[key] -= 1
            else:
                print(arr[idx],k,arr[idx]%k,(arr[idx]%k or k))
                lookup[arr[idx]%k or k] += 1
        return cnt == l//2
            