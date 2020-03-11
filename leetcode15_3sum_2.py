# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
  # [-1, 0, 1],
  # [-1, -1, 2]
# ]

import datetime
def find_triplet(nums):
	l = len(nums)
	
	print(nums) if debug else None
	if l < 3:
		return []
		
	
	nums = sorted(nums)
	print(nums) if debug else None
	
	cache = [[None for c in range(l)] for r in range(l-1)]
	#print(cache) if debug else None
	
	for r in range(l-1):
		#print(r)
		if r > 0:
			if nums[r-1] == nums[r]:
				continue
		for c in range(r+1,l):
			#print(r,c)
			if c-r > 1:
				if nums[c-1] != nums[c]:
					cache[r][c] = nums[r] + nums[c]
			else:
				cache[r][c] = nums[r] + nums[c]
			
	print(cache) if debug else None
	op = []
	for r in range(l-1):
		for c in range(r+1,l):
			if cache[r][c] is not None:
				for j in range(c+1,l):
					if cache[r][c] + nums[j] == 0:
						if j-c > 1:
							if nums[j] != nums[j-1]:
								print(cache[r][c],nums[r],nums[c],nums[j]) if debug else None
								op.append([nums[r],nums[c],nums[j]])
						else:
							print(cache[r][c],nums[r],nums[c],nums[j]) if debug else None
							op.append([nums[r],nums[c],nums[j]])
						
						
	print(op) if debug else None
	return op
	
debug = False
#debug = True
print(find_triplet([-1,-1,2]))
print(find_triplet( [-1,0,1,2,-1,-4]))
print(find_triplet([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(find_triplet( [0,0,0,0]))
