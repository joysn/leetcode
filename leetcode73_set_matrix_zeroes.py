# https://leetcode.com/problems/set-matrix-zeroes/
# 73. Set Matrix Zeroes
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
# Example 1:
# Input: 
# [
  # [1,1,1],
  # [1,0,1],
  # [1,1,1]
# ]
# Output: 
# [
  # [1,0,1],
  # [0,0,0],
  # [1,0,1]
# ]
# Example 2:
# Input: 
# [
  # [0,1,2,0],
  # [3,4,5,2],
  # [1,3,1,5]
# ]
# Output: 
# [
  # [0,0,0,0],
  # [0,4,5,0],
  # [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if matrix is None:
            return matirx
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 1 and cols == 1:
            return [[1]]
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is not None:
                    if matrix[r][c] == 0:
                        for i in range(rows):
                            if matrix[i][c] != 0:
                                matrix[i][c] = None
                        for j in range(cols):
                            if matrix[r][j] != 0:
                                matrix[r][j] = None
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is None:
                    matrix[r][c] = 0
                        
