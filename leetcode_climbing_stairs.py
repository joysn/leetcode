# https://leetcode.com/problems/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n : int) -> int:
	
	cache = [0 for i in range(n+1)]
	
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 2
	
	cache[1] = 1
	cache[2] = 2
	
	for curr_stair in range(3,n+1):
		cache[curr_stair] = cache[curr_stair-1] + cache[curr_stair-2] 
		
	return cache[n]
	
	
for i in range(6):
	print("Climb {} stairs in {} ways".format(i,climbStairs(i)))
		
		
# (base) D:\>python leetcode_climbing_stairs.py
# Climb 0 stairs in 0 ways
# Climb 1 stairs in 1 ways
# Climb 2 stairs in 2 ways
# Climb 3 stairs in 3 ways
# Climb 4 stairs in 5 ways
# Climb 5 stairs in 8 ways
		
