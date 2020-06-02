# https://leetcode.com/problems/reverse-pairs/
# 493. Reverse Pairs
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# You need to return the number of important reverse pairs in the given array.
# Example1:
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.

def binsearch(nums,s,l,r):
	print("Called with",nums,s,l,r) if debug else None
	#return 0
	mid = (l+r)//2
	cnt = 0
	found = 0
	while l < r:
		cnt += 1
		print("......Str:",nums[mid],l,mid,r) if debug else None
		if nums[mid] > s:
			r = mid - 1
		elif nums[mid] < s:
			if mid + 1 < l:
				l = mid+1
		else:
			print("Return1-",mid+1) if debug else None
			return mid+1
		print("......End:",nums[mid],l,mid,r) if debug else None
		#if cnt == 10:
		#	break
	
	if l < 0:
		print("Return21-",0) if debug else None
		return 0
	if r <= l:
		if nums[l] <= s:
			print("Return22-",1) if debug else None
			return 1
		else:
			print("Return23-",0) if debug else None
			return 0
	print("Return3-",mid) if debug else None
	return mid
	
#binsearch([1, 2, 3, 3],0,0,3)
#binsearch([1, 2, 3],1,0,2)
import math
def reversePairs(nums) -> int:
	l = len(nums)
	if l < 2:
		return 0
		
	cnt = 0
	for i in range(l-1):
		num_right = math.ceil(nums[i]/2) - 1
		print(nums[i],num_right) if debug else None
		
		sorted_nums = nums[i+1:]
		sorted_nums = sorted(sorted_nums)
		cnt += binsearch(sorted_nums,num_right,0,len(sorted_nums)-1)
		print("New count for",sorted_nums,"is:",cnt) if debug else None
			
	return cnt
	
debug = False
#debug = True
print("********* Way 1 ************")
print(reversePairs([1,3,2,3,1])== 2)
print(reversePairs([2,4,3,5,1])== 3)
print(reversePairs([1,1,3,2,3])== 0)

import bisect
def reversePairs(nums) -> int:
	l = len(nums)
	if l < 2:
		return 0

	sorted_nums = sorted(nums)
	print(nums) if debug else None
	print(sorted_nums) if debug else None
	count = 0
	for num in nums: # O(N)
		print("Idx to be deleted from",sorted_nums," for",num,"is:",sorted_nums.index(num)) if debug else None
		del sorted_nums[bisect.bisect_left(sorted_nums, num)] # O(logN)
		idx = bisect.bisect_left(sorted_nums, num/2)
		count += idx
	return count
	
debug = False
#debug = True
print("********* Way 2 ************")
print(reversePairs([1,3,2,3,1])== 2)
print(reversePairs([2,4,3,5,1])== 3)
print(reversePairs([1,1,3,2,3])== 0)


# (base) D:\>python leetcode493_reverse_pairs.py
# ********* Way 1 ************
# True
# True
# True
# ********* Way 2 ************
# True
# True
# True
	
	