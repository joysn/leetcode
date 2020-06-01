# https://leetcode.com/problems/island-perimeter/
# 463. Island Perimeter
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
 # [1,1,1,0],
 # [0,1,0,0],
 # [1,1,0,0]]

# Output: 16

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        c = len(grid[0])
        r = len(grid)
        permiter = 0
        
                    
        for ir in range(r):
            for ic in range(c):
                if grid[ir][ic] == 1:
                    if ir - 1 >= 0:
                        if grid[ir-1][ic] != 1:
                            permiter += 1
                    else:
                        permiter += 1
                    if ir+1 < r:
                        if grid[ir+1][ic] != 1:
                            permiter += 1
                    else:
                        permiter += 1
                    if ic - 1 >= 0:
                        if grid[ir][ic-1] != 1:
                            permiter += 1
                    else:
                        permiter += 1
                    if ic + 1 < c:
                        if grid[ir][ic+1] != 1:
                            permiter += 1
                    else:
                        permiter += 1
                #print("For row",ir,"and column",ic,"Permiter count is",permiter)
            #print("For row",ir,"Permiter count is",permiter)
        return permiter