# https://leetcode.com/problems/subsets/
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# Example:
# Input: nums = [1,2,3]
# Output:
# [
  # [3],
  # [1],
  # [2],
  # [1,2,3],
  # [1,3],
  # [2,3],
  # [1,2],
  # []
# ]

import copy
def subsets_helper(nums):
	print("Called",nums) if debug else None
	l = len(nums)
	
	if l == 1:
		print("Return:",[nums]) if debug else None
		return [nums]
        
	op= [[nums[-1]]]
	op_re = subsets_helper(nums[:-1])
	for e in op_re:
		print("... Before E",e) if debug else None
		op.append(e)
		t = copy.deepcopy(e)
		t.append(nums[-1])
		print("... After E",t) if debug else None
		op.append(t)
		
	print("Return",op) if debug else None
	return op
	
def subsets( nums):
	l = len(nums)
	if l == 0:
		print("Return []") if debug else None
		return [[]]
	op = subsets_helper(nums)
	op.append([])
	
	return op
	
debug = False
#debug = True
print(subsets([1,2,3]))
