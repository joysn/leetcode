# https://leetcode.com/problems/sort-the-matrix-diagonally/
# 1329. Sort the Matrix Diagonally
# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

# Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        if mat is None:
            return mat
        if mat == []:
            return mat
        
        rows = len(mat)
        cols = len(mat[0])
        
        
        for r in range(rows-1,-1,-1):
            t_col = sorted([mat[r+i][i] for i in range(min(rows-r,cols))])
            for i in range(min(rows-r,cols)):
                mat[r+i][i] = t_col[i]
        
        if rows == 1:
            return mat
        for c in range(1,cols):
            t_col = sorted([mat[i][c+i] for i in range(min(cols-c,rows))])

            for i in range(min(cols-c,rows)):
                mat[i][c+i] = t_col[i]
        
  
        return mat