# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if board is None:
            return
        rows = len(board)
        if rows == 0:
            return board
        cols = len(board[0])
        
        
        if rows == 1 and cols == 1:
            return board
        
        def visit(o_list):
            while len(o_list) != 0:
                r,c = o_list.pop()
                #print(r,c)
                if c-1 >= 0:
                    if board[r][c-1] == "O":
                        board[r][c-1] = "Y"
                        o_list.append((r,c-1))
                if c+1 <= cols-1:
                    if board[r][c+1] == "O":
                        board[r][c+1] = "Y"
                        o_list.append((r,c+1))
                if r-1 >= 0:
                    if board[r-1][c] == "O":
                        board[r-1][c] = "Y"
                        o_list.append((r-1,c))
                if r+1 <= rows - 1:
                    if board[r+1][c] == "O":
                        board[r+1][c] = "Y"
                        o_list.append((r+1,c))
            
                            
        # revolve round the boudaries to check for o
        offset_c = 0
        offset_r = 0
        for c in range(offset_c,cols-2-offset_c+1):
            if board[offset_r][c] == "O":
                board[offset_r][c] = "Y"
                visit([(offset_r,c)])
        for r in range(offset_r,rows-2-offset_r+1):
            if board[r][cols-1-offset_c] == "O":
                board[r][cols-1-offset_c] = "Y"
                visit([(r,cols-1-offset_c)])
        for c in range(cols-1-offset_c,offset_c-1+1,-1):
            if board[rows-1-offset_r][c] == "O":
                board[rows-1-offset_r][c] = "Y"
                visit([(rows-1-offset_r,c)])
        for r in range(rows-1-offset_r,offset_r-1+1,-1):
            if board[r][offset_c] == "O":
                board[r][offset_c] = "Y"
                visit([(r,offset_c)])
                
        
        #print(board)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Y":
                    board[r][c] = "O"
                    
        