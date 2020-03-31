# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

import sys

def minSubArrayLen(s, nums):
        
	#nums = [1,2,3,4,5]
	#s = 11
	l = len(nums)

	if l == 0:
		return 0
	
	mn = sys.maxsize
	found = 0
	for c in range(l):
		if nums[c] >= s:
			return 1

	for r in range(l):
		cache = [0 for c in range(l)]
		for c in range(r,l):
			if r == c:
				cache[c] = nums[c]
			else:
				cache[c] = cache[c-1] + nums[c]
			if cache[c] >= s:
				found = 1
				if mn > c-r+1:
					mn = c-r+1
		#print(cache)
            
	if found == 0:
		return 0
	return mn
	
print("*****************************")
print("********* Using DP *********")
print("*****************************")
print(minSubArrayLen(7,[2,3,1,2,4,3]) == 2)
print(minSubArrayLen(4,[1,4,4]) == 1)
print(minSubArrayLen(100,[]) == 0)
print(minSubArrayLen(11,[1,2,3,4,5]) == 3)


from queue import Queue
def minSubArrayLen(s, nums):
        
	l = len(nums)

	if l == 0:
		return 0
	
	mn = sys.maxsize
	found = 0
	for c in range(l):
		if nums[c] >= s:
			return 1
			
	sm = 0
	q = Queue()
	for r in range(l):
		sm += nums[r]
		q.put(r)
		if sm >= s:
			found = 1
			if q.qsize() < mn:
				mn = q.qsize()
			while True:
				tidx = q.get()
				sm -= nums[tidx]
				if sm >= s:
					mn = q.qsize()
				else:
					break
			
	if found == 0:
		return 0
	return mn

debug = True
debug = False
print("*******************************")
print("********* Using Queue *********")
print("*******************************")
print(minSubArrayLen(7,[2,3,1,2,4,3]) == 2)
print(minSubArrayLen(4,[1,4,4]) == 1)
print(minSubArrayLen(100,[]) == 0)
print(minSubArrayLen(11,[1,2,3,4,5]) == 3)



def minSubArrayLen(s, nums):
        
	l = len(nums)

	if l == 0:
		return 0
	
	found = 0
	for c in range(l):
		if nums[c] >= s:
			return 1
			
	sm = 0
	mn = l+1
	left = 0
	right = 0
	while right < l:
		while sm < s and right < l:
			sm += nums[right]
			right += 1
		while sm >= s and left < l:
			mn = min(mn, right -left)
			sm -= nums[left]
			left += 1
	return 0 if mn == l+1 else mn

debug = True
debug = False
print("***********************************")
print("********* Using 2 pointer *********")
print("***********************************")
print(minSubArrayLen(7,[2,3,1,2,4,3]) == 2)
print(minSubArrayLen(4,[1,4,4]) == 1)
print(minSubArrayLen(100,[]) == 0)
print(minSubArrayLen(11,[1,2,3,4,5]) == 3)