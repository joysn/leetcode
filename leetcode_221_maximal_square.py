# https://leetcode.com/problems/maximal-square/
# 221. Maximal Square
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if matrix == None:
            return 0
            
        r = len(matrix)
        c = len(matrix[0])
        print(r,c)
        
        max_sq_len = 0
        
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    max_sq_len = 1
        
        
                
        for i in range(r-1,0,-1):
            for j in range(c-1,0,-1):
                if matrix[i-1][j-1] == 0:
                    continue
                matrix[i-1][j-1] += min(matrix[i][j],matrix[i][j-1],matrix[i-1][j]) 
                if max_sq_len < matrix[i-1][j-1]:
                    max_sq_len = matrix[i-1][j-1]
        
        return max_sq_len*max_sq_len
        
