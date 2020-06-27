# https://leetcode.com/problems/unique-paths/submissions/
# 62. Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Above is a 7 x 3 grid. How many possible unique paths are there?
# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28
# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        
        cache = [[0 for c in range(n)] for r in range(m)]
        
        cache[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r-1 >= 0:
                    cache[r][c] += cache[r-1][c]
                if c-1 >= 0:
                    cache[r][c] += cache[r][c-1]
                    
        #print(cache)         
        return cache[m-1][n-1]
        