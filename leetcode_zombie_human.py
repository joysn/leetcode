# https://leetcode.com/discuss/interview-experience/508224/amazon-sde-1-feb-2020-reject

# https://leetcode.com/discuss/interview-question/411357/
# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

# Example:

# Input:
# [[0, 1, 1, 0, 1],
 # [0, 1, 0, 1, 0],
 # [0, 0, 0, 0, 1],
 # [0, 1, 0, 0, 0]]

# Output: 2

# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
 # [1, 1, 1, 1, 1],
 # [0, 1, 0, 1, 1],
 # [1, 1, 1, 0, 1]]

# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
 # [1, 1, 1, 1, 1],
 # [1, 1, 1, 1, 1],
 # [1, 1, 1, 1, 1]]
# int minHours(int rows, int columns, List<List<Integer>> grid) {
	# // todo
# }

# n = # of humans + zombie (size of grid)
# h = # of humans
# z = # of zombie
# t = seconds to cover

# Time = O(h+z)*t
# Space = constant

def find_extinction_time(human_grid):
	
	rows = len(human_grid)
	if rows == 0:
		return
	cols = len(human_grid[0])
	
	
	
	time = 0
	while True:
		convert = 0
		time += 1
		for r in range(rows):
			for c in range(cols):
				if human_grid[r][c] == 1:
					if c-1 > 0:
						if human_grid[r][c-1] == 0:
							convert = 1
							human_grid[r][c-1] = 1
					if c+1 < cols:
						if human_grid[r][c+1] == 0:
							convert = 1
							human_grid[r][c+1] = 1
					if r-1 > 0:
						if human_grid[r-1][c] == 0:
							convert = 1
							human_grid[r-1][c] = 1
					if r+1 < rows:
						if human_grid[r+1][c] == 0:
							convert = 1
							human_grid[r+1][c] = 1
		if convert == 0:
			break
			
	#print(time)
	return time
	
hg = [[0, 1, 1, 0, 1],\
  [0, 1, 0, 1, 0],\
  [0, 0, 0, 0, 1],\
  [0, 1, 0, 0, 0]]
  
print("Time remaining for human extinction",find_extinction_time(hg))


# Time = O(n) + logn
# Space = O(n)

import queue
def find_extinction_time(human_grid):
	
	rows = len(human_grid)
	if rows == 0:
		return
	cols = len(human_grid[0])
	
	q1 = queue.Queue()
	q2 = queue.Queue()
	
	for r in range(rows):
		for c in range(cols):
			if human_grid[r][c] == 1:
				q1.put((r,c))
				#print(r,c)

	time = 0
	while True:
		q2 = queue.Queue()
		while not q1.empty():
			zombie = q1.get()
			r = zombie[0]
			c = zombie[1]
			if c-1 >= 0:
				if human_grid[r][c-1] == 0:
					human_grid[r][c-1] = 1
					q2.put((r,c-1))
					print(time,r,c-1) if debug else None
			if c+1 < cols:
				if human_grid[r][c+1] == 0:
					human_grid[r][c+1] = 1
					q2.put((r,c+1))
					print(time,r,c+1) if debug else None
			if r-1 >= 0:
				if human_grid[r-1][c] == 0:
					human_grid[r-1][c] = 1
					q2.put((r-1,c))
					print(time,r-1,c) if debug else None
			if r+1 < rows:
				if human_grid[r+1][c] == 0:
					human_grid[r+1][c] = 1
					q2.put((r+1,c))
					print(time,r+1,c) if debug else None

		print("Size of q2",q2.qsize())  if debug else None
		if q2.empty():
			print("Q2 is empty!!!") if debug else None
			break
		time += 1
		q1 = q2
		
	return time
	
debug = True
debug = False
hg = [[0, 1, 1, 0, 1],\
  [0, 1, 0, 1, 0],\
  [0, 0, 0, 0, 1],\
  [0, 1, 0, 0, 0]]
print("Time remaining for human extinction",find_extinction_time(hg))


def find_extinction_time(human_grid):
	
	rows = len(human_grid)
	if rows == 0:
		return
	cols = len(human_grid[0])
	
	q1 = queue.Queue()
	q2 = queue.Queue()
	
	for r in range(rows):
		for c in range(cols):
			if human_grid[r][c] == 1:
				q1.put((r,c))
				#print(r,c)

	time = 0
	while True:
		q2 = queue.Queue()
		while not q1.empty():
			zombie = q1.get()
			r = zombie[0]
			c = zombie[1]
			if c-1 >= 0:
				if human_grid[r][c-1] == 0:
					human_grid[r][c-1] = 1
					q2.put((r,c-1))
					print(time,r,c-1) if debug else None
			if c+1 < cols:
				if human_grid[r][c+1] == 0:
					human_grid[r][c+1] = 1
					q2.put((r,c+1))
					print(time,r,c+1) if debug else None
			if r-1 >= 0:
				if human_grid[r-1][c] == 0:
					human_grid[r-1][c] = 1
					q2.put((r-1,c))
					print(time,r-1,c) if debug else None
			if r+1 < rows:
				if human_grid[r+1][c] == 0:
					human_grid[r+1][c] = 1
					q2.put((r+1,c))
					print(time,r+1,c) if debug else None

		print("Size of q2",q2.qsize())  if debug else None
		if q2.empty():
			print("Q2 is empty!!!") if debug else None
			break
		time += 1
		q1 = q2
		
	return time