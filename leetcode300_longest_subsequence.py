# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

def lengthOfLIS(nums) -> int:
	l = len(nums)
	
	if l <= 1:
		return l
		
	cache = [1]*l
	
	max_len = 1
	for i in range(1,l):
		for j in range(i):
			#print("For",nums[i],nums[j]) if debug else None
			if nums[j] < nums[i]:
				
				cache[i] = max(cache[i],cache[j]+1)
		
		if max_len < cache[i]:
			max_len = cache[i]
			
	print(cache) if debug else None
	print(max_len) if debug else None
	return max_len
	
	
debug = False
print(lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
print(lengthOfLIS([]) == 0)
print(lengthOfLIS([1]) == 1)
print(lengthOfLIS([10,9,2,5,3,7,101,18,102,103]) == 6)
print(lengthOfLIS([1,2]) == 2)
print(lengthOfLIS([1,19,2,20,3,4,21,22,23,18,19]) == 7)


# (base) D:\>python leetcode300_longest_subsequence.py
# True
# True
# True
# True
# True
# True