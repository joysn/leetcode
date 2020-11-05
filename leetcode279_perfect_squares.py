# https://leetcode.com/problems/perfect-squares/
# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example 1:
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:
        
        if n <= 1:
            return n
        psquares = []
        for i in range(1,n):
            ps = i*i
            if ps > n:
                break
            psquares.append(ps)
            
        cnt = collections.Counter(psquares)
        cache = [0]*(n+1)
        for k in cnt:
            q = n//k
            for i in range(q+1):
                cache[k*i] = i
            
        prev = 1
        for i in range(2,n+1):
            if cache[i] == 1:
                prev = i
            else:
                for p in psquares:
                    if p > i:
                        break
                    cache[i] = min(cache[i],cache[p]+cache[i-p])
        return cache[-1]