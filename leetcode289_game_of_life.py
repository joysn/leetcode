# https://leetcode.com/problems/game-of-life/
# 289. Game of Life
# Medium
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input: 
# [
  # [0,1,0],
  # [0,0,1],
  # [1,1,1],
  # [0,0,0]
# ]
# Output: 
# [
  # [0,0,0],
  # [1,0,1],
  # [0,1,1],
  # [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        if rows == 0 or cols == 0:
            return
        
        if rows == 1 and cols == 1:
            board[0][0] = 0
            return
                
        for r in range(rows):
            for c in range(cols):
                count = 0
                if r-1 >= 0 and c-1 >= 0:
                    if board[r-1][c-1] >= 1:
                        count += 1
                if r-1 >= 0:
                    if board[r-1][c] >= 1:
                        count += 1
                if r-1 >= 0 and c+1 < cols:
                    if board[r-1][c+1] >= 1:
                        count += 1
                if c-1 >= 0:
                    if board[r][c-1] >= 1:
                        count += 1
                if c+1 < cols:
                    if board[r][c+1] >= 1:
                        count += 1
                if r+1 < rows and c-1 >= 0:
                    if board[r+1][c-1] >= 1:
                        count += 1
                if r+1 < rows:
                    if board[r+1][c] >= 1:
                        count += 1
                if r+1 < rows and c+1 < cols:
                    if board[r+1][c+1] >= 1:
                        count += 1
                
                #print("for r and c",r,c," count is ",count)
                # For live cell
                if board[r][c] == 1:
                    if count < 2:
                        board[r][c] = 2
                    elif count <= 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 2
                else:
                    if count == 3:
                        board[r][c] = -1
                
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                if board[r][c] == -1:
                    board[r][c] = 1
                    
                
                    
                    
        