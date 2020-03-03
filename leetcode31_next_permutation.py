# https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


def swap(nums,a,b):
	temp = nums[a]
	nums[a] = nums[b]
	nums[b] = temp
	return nums
	
def nextPermutation(nums):
    
	length = len(nums)
	if length == 0:
		return
		
	if length == 1:
		return
		
	if length == 2:
		nums = nums[::-1]
		return
		
	done = False
	source = length-2
	while not done:
		print(source) if debug else None
		for dest in range(length-1,source,-1):
			print(source,dest) if debug else None
			if nums[source] < nums[dest]:
				temp = nums[source]
				nums[source] = nums[dest]
				nums[dest] = temp
				print(source,dest,nums) if debug else None
				nums[source+1:] = sorted(nums[source+1:])
				done = True
				break
		if done is not True:
			source = source - 1
		if source < 0:
			nums = sorted(nums)
			done = True
		#print(nums)
				
	return nums


debug = False
print("[1,2,3] ->",nextPermutation([1,2,3]))
print("[1,3,2] ->",nextPermutation([1,3,2]))
print("[2,1,3] ->",nextPermutation([2,1,3]))
print("[2,3,1] ->",nextPermutation([2,3,1]))
print("[3,1,2] ->",nextPermutation([3,1,2]))
print("[3,2,1] ->",nextPermutation([3,2,1]))
print("[4,2,0,2,3,2,0]->",nextPermutation([4,2,0,2,3,2,0]))