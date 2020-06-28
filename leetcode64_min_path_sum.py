# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:
# Input:
# [
  # [1,3,1],
  # [1,5,1],
  # [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        if grid is None:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 1 and cols == 1:
            return grid[0][0]
        
        
        cache = [[0 for c in range(cols)] for r in range(rows)]
        
        cache[0][0] = grid[0][0]
        
        for r in range(rows):
            for c in range(cols):
                up_val = None
                left_val = None
                
                if r == 0 and c == 0:
                    continue
                if r-1 >= 0:
                    up_val = cache[r-1][c]
                if c-1 >= 0:
                    left_val = cache[r][c-1]
                if up_val is None:
                    min_val = left_val
                elif left_val is None:
                    min_val = up_val
                else:
                    min_val = min(up_val,left_val)
                #print("...",r,c,min_val)
                cache[r][c] = grid[r][c] + min_val
              
        #print(cache)
        return cache[rows-1][cols-1]
        
        
        