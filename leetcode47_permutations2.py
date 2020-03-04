# https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
  # [1,1,2],
  # [1,2,1],
  # [2,1,1]
# ]

import copy
def permutations(nums):
	
	
	length = len(nums)
	if length == 0:
		return nums
	if length == 1:
		return nums
		
		
	cache = [[] for c in range(length)]
	cache[0] = [[nums[0]]]
	print(cache) if debug else None
	
	for c in range(1,length):
		prev_list = cache[c-1]
		#print("1:",prev_list)
		curr_list = []
		for plist in prev_list:
			print("2 plist:",plist) if debug else None
			for idx in range(len(plist)+1):
				l1 = copy.deepcopy(plist)
				l1 = l1[0:idx] + [nums[c]] + l1[idx:]
				if l1 not in curr_list:
					curr_list.append(l1)
		cache[c] = copy.deepcopy(curr_list)
		
	print(cache) if debug else None
	return cache[length-1]
	
debug = False
print(permutations([1,1]))
print(permutations([1,2]))
#debug = True
print(permutations([1,2,3]))
print(permutations([1,1,2]))