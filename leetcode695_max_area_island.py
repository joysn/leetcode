# https://leetcode.com/problems/max-area-of-island/
# 695. Max Area of Island
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 # [0,0,0,0,0,0,0,1,1,1,0,0,0],
 # [0,1,1,0,1,0,0,0,0,0,0,0,0],
 # [0,1,0,0,1,1,0,0,1,0,1,0,0],
 # [0,1,0,0,1,1,0,0,1,1,1,0,0],
 # [0,0,0,0,0,0,0,0,0,0,1,0,0],
 # [0,0,0,0,0,0,0,1,1,1,0,0,0],
 # [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if grid is None:
            return 0
        
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        def measure_island(island):
            count = 1
            while len(island) != 0:
                r,c = island.pop()
                if c-1 >= 0:
                    if grid[r][c-1] == 1:
                        island.append((r,c-1))
                        grid[r][c-1] = 2
                        count += 1
                if c+1 <= cols -1:
                    if grid[r][c+1] == 1:
                        island.append((r,c+1))
                        grid[r][c+1] = 2
                        count += 1
                if r-1 >= 0:
                    if grid[r-1][c] == 1:
                        island.append((r-1,c))
                        grid[r-1][c] = 2
                        count += 1
                if r+1 <= rows-1:
                    if grid[r+1][c] == 1:
                        island.append((r+1,c))
                        grid[r+1][c] = 2
                        count += 1
            return count
        
        max_size = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    sz = measure_island([(r,c)])
                    #print("For ",r,c," count is ",sz)
                    if sz > max_size:
                        max_size = sz
                       
        #print(grid)
        return max_size
        
        