# https://leetcode.com/problems/path-with-maximum-gold/
# 1219. Path with Maximum Gold
# In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

# Every time you are located in a cell you will collect all the gold in that cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
# Example 1:
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
 # [5,8,7],
 # [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# Example 2:
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
 # [2,0,6],
 # [3,4,5],
 # [0,3,0],
 # [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
# Constraints:
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.

global maxGold 
maxGold = 0
def getMaximumGold( grid) -> int:
	global maxGold
	def collect(r,c,total=0):
		#print("Called with",r,c)
		global maxGold
		total += grid[r][c]
		tmp = grid[r][c]
		grid[r][c] = 0
		
		if maxGold < total:
			maxGold = total
		
		for gapr,gapc in ((-1,0),(1,0),(0,1),(0,-1)):
			newr,newc = r+gapr, c+gapc
			if not (0<=newc<csize and 0<=newr<rsize and grid[newr][newc] != 0):
				continue
			collect(newr,newc,total)
		grid[r][c] = tmp
		#print(total)
        
	rsize = len(grid)
	csize = len(grid[0])
	for r in range(rsize):
		for c in range(csize):
			if grid[r][c] != 0:
				collect(r,c,0)
				
	return maxGold
                
maxGold = 0
print(getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])==24)
maxGold = 0
print(getMaximumGold([[0,6],[5,8]])==19)
#print("MaxGold is",maxGold)