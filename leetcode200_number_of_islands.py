# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        
        edge = []
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    #print("inside if")
                    edge.append((r,c))
                    grid[r][c] = 0
                    #print("Start at",edge)
                    while len(edge) != 0:
                        #print(edge)
                        if edge[0][1]+1 < cols:
                            if grid[edge[0][0]][edge[0][1]+1] == '1':
                                edge.append((edge[0][0],edge[0][1]+1))
                                grid[edge[0][0]][edge[0][1]+1] = 0
                        if edge[0][1]-1 >= 0:
                            if grid[edge[0][0]][edge[0][1]-1] == '1':
                                edge.append((edge[0][0],edge[0][1]-1))
                                grid[edge[0][0]][edge[0][1]-1] = 0
                        if edge[0][0]+1 < rows:
                            if grid[edge[0][0]+1][edge[0][1]] == '1':
                                edge.append((edge[0][0]+1,edge[0][1]))
                                grid[edge[0][0]+1][edge[0][1]] = 0
                        if edge[0][0]-1 >= 0:
                            if grid[edge[0][0]-1][edge[0][1]] == '1':
                                edge.append((edge[0][0]-1,edge[0][1]))
                                grid[edge[0][0]-1][edge[0][1]] = 0
                        del edge[0]
                    count += 1
        return count