# https://leetcode.com/problems/coloring-a-border/
# 1034. Coloring A Border
# Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.
# Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.
# The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).
# Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

# Example 1:
# Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# Output: [[3, 3], [3, 2]]
# Example 2:
# Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# Output: [[1, 3, 3], [2, 3, 3]]
# Example 3:
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        sColor = grid[r0][c0]
        
        boundary = set()
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        tree = set([(r0,c0)])
        while len(tree) > 0:
            node = tree.pop()
            print(node)
            r = node[0]
            c = node[1]
            if grid[r][c] < 0:
                # already visited
                continue
            grid[r][c] *= -1
            
            if r == 0 or c == 0 or r == rows-1 or c == cols - 1:
                boundary.add(node)
            if r-1 >= 0:
                if abs(grid[r-1][c]) != sColor:
                    boundary.add(node)
                else:
                    tree.add((r-1,c))
            if r+1 < rows:
                if abs(grid[r+1][c]) != sColor:
                    boundary.add(node)
                else:
                    tree.add((r+1,c))
            if c-1 >= 0:
                if abs(grid[r][c-1]) != sColor:
                    boundary.add(node)
                else:
                    tree.add((r,c-1))
            if c+1 < cols:
                if abs(grid[r][c+1]) != sColor:
                    boundary.add(node)
                else:
                    tree.add((r,c+1))
            #print(tree)
            #print(boundary)
        
        #print(boundary)
        for e in boundary:
            grid[e[0]][e[1]] = color
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    grid[r][c] *= -1
        
        return grid
                    
                
        