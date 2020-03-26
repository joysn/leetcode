# https://leetcode.com/problems/contiguous-array/
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

def findMaxLength(nums):

	l = len(nums)
	if l == 0 or l == 1:
		return 0
	if l == 2:
		if nums[0] != nums[1]:
			return l
		else:
			return 0
			
	z_count = nums.count(0)
	o_count = nums.count(1)
	print(z_count,o_count) if debug else None
	if z_count == o_count:
		return l
		
	c1 = 0
	c2 = 0
	c1 = findMaxLength(nums[1:])
	c2 = findMaxLength(nums[:-1])
	print(c1,c2) if debug else None
	if c1 > c2:
		return c1
	else:
		return c2

debug = True
debug = False	
print("#################################")	
print("######## Using Recursion ########")
print("#################################")	
print(findMaxLength([0,1]) == 2,":2")
print(findMaxLength([0,1,0]) == 2,":2")
print(findMaxLength([0,1,1,0,1,1,1,0]) == 4,":4")
print(findMaxLength([0,1,0,1]) == 4,":4")
print(findMaxLength([0,0,0,1,1,1,0]) == 6,":6")
print(findMaxLength([0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1]) == 8,":8")
print(findMaxLength([0,0,1,0,0,0,1,1]) == 6,":6")

def findMaxLength(nums):
	l = len(nums)
	if l == 0 or l == 1:
		return 0
	if l == 2:
		if nums[0] != nums[1]:
			return 2
		else:
			return 0
            
	if l == 3:
		if nums[0] != nums[1] or nums[1] != nums[2]:
			return 2
	mx = 0
		
	for r in range(l):
		if l-r-1 < mx*2:
			continue
		prev_z = 0
		prev_o = 0
		for c in range(0+r,l):
			if c == 0:
				if nums[r] == 0:
					prev_z = 1
					prev_o = 0
				else:
					prev_z = 0
					prev_o = 1
			elif nums[c] == 0:
				prev_z += 1
			else:
				prev_o += 1
			if prev_z == prev_o:
				if mx < prev_z:
					mx = prev_z
				print(mx) if debug else None
	print(mx*2,end=":") if debug else None
	return mx*2
		
debug = True
debug = False	
print("####################")	
print("###### DP - 1 ######")
print("####################")	
print(findMaxLength([0,1]) == 2,":2")
print(findMaxLength([0,1,0]) == 2,":2")
print(findMaxLength([0,1,1,0,1,1,1,0]) == 4,":4")
print(findMaxLength([0,1,0,1]) == 4,":4")
print(findMaxLength([0,0,0,1,1,1,0]) == 6,":6")
print(findMaxLength([0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1]) == 8,":8")
print(findMaxLength([0,0,1,0,0,0,1,1]) == 6,":6")




def findMaxLength(nums):
	curr = res = 0
	seen = {0 : 0}
	for i, num in enumerate(nums):
		curr += 1 if num else -1
		print(i,num,curr,res,seen) if debug else None
		if curr in seen:
			res = max(res, i - seen[curr] if curr != 0 else i + 1)
		else:
			seen[curr] = i
		print("After res,seen",i,num,curr,res,seen) if debug else None
	return res


debug = True
debug = False	
print("#####################")	
print("###### HashMap ######")
print("#####################")	
print(findMaxLength([0,1]) == 2,":2")
print(findMaxLength([0,1,0]) == 2,":2")
print(findMaxLength([0,1,1,0,1,1,1,0]) == 4,":4")
print(findMaxLength([0,1,0,1]) == 4,":4")
print(findMaxLength([0,0,0,1,1,1,0]) == 6,":6")
print(findMaxLength([0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1]) == 8,":8")
print(findMaxLength([0,0,1,0,0,0,1,1]) == 6,":6")



# (base) D:\>python leetcode_contiguous_array.py
# #################################
# ######## Using Recursion ########
# #################################
# True :2
# True :2
# True :4
# True :4
# True :6
# True :8
# True :6
# ####################
# ###### DP - 1 ######
# ####################
# True :2
# True :2
# True :4
# True :4
# True :6
# True :8
# True :6
# #####################
# ###### HashMap ######
# #####################
# True :2
# True :2
# True :4
# True :4
# True :6
# True :8
# True :6

