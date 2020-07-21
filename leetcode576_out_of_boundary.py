# https://leetcode.com/problems/out-of-boundary-paths/
# 576. Out of Boundary Paths
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
# Example 1:
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# Example 2:
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation
# Note:
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        cache = {}
        
        def dfs(r,c,step):
            if step > N:
                return 0
            
            if r < 0 or c < 0 or r >= m or c >= n:
                if step <= N:
                    return 1
                return 0
            
            if (r,c,step) in cache:
                return cache[(r,c,step)]
            
            cache[(r,c,step)] = dfs(r+1,c,step+1)+dfs(r,c+1,step+1)+dfs(r-1,c,step+1)+dfs(r,c-1,step+1)
            return (cache[(r,c,step)]%((10**9)+7))
            
        return dfs(i,j,0)