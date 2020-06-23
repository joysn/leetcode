# https://leetcode.com/problems/unique-paths-ii/submissions/
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?



# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
  # [0,0,0],
  # [0,1,0],
  # [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        cache = [[0 for c in range(cols)] for r in range(rows)]
        cache[0][0] = 1
        
        debug = False
        for r in range(rows):
            for c in range(cols):
                print("...",r,c) if debug else None
                if obstacleGrid[r][c] == 1:
                    continue
                if r-1 >= 0:
                    if obstacleGrid[r-1][c] == 0:
                        cache[r][c] += cache[r-1][c]
                if c-1 >= 0:
                    if obstacleGrid[r][c-1] == 0:
                        cache[r][c] += cache[r][c-1]
        print(cache) if debug else None
        return cache[rows-1][cols-1]

        

        