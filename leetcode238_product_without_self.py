# https://leetcode.com/problems/product-of-array-except-self/
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

def productExceptSelf(nums):
	
	l = len(nums)
	prod = [0 for i in range(l)]
	prod[0] = nums[0]
	for i in range(1,l):
		prod[i] = prod[i-1]*nums[i]
		
	print(prod) if debug else None
	
	rev_prod = [0 for i in range(l)]
	rev_prod[l-1] = nums[l-1]
	for i in range(l-2,-1,-1):
		rev_prod[i] = rev_prod[i+1]*nums[i]
	print(rev_prod) if debug else None
	
	
	op = [0 for i in range(l)]
	op[0] = rev_prod[1]
	for i in range(1,l-1):
		op[i] = prod[i-1]*rev_prod[i+1]
	op[l-1] = prod[l-2]
	
	print(op) if debug else None
	return op
	
debug = False
#debug = True
print("**** time = O(n) and space = O(n) *****")
print(productExceptSelf([1,2,3,4]) == [24,12,8,6])



def productExceptSelf(nums):
	
	l = len(nums)
	
	op = [0 for i in range(l)]
	op[l-1] = nums[l-1]
	for i in range(l-2,-1,-1):
		op[i] = op[i+1]*nums[i]
	print(op) if debug else None
	
	
	op[0] = op[1]
	curr = nums[0]
	for i in range(1,l-1):
		prev = curr
		curr = prev * nums[i]
		next = op[i+1]
		op[i] = prev*next
	op[l-1] = curr
	
	print(op) if debug else None
	return op
	
debug = False
#debug = True
print("**** time = O(n) and space = C *****")
print(productExceptSelf([1,2,3,4]) == [24,12,8,6])


# (base) D:\>python leetcode238_product_without_self.py
# **** time = O(n) and space = O(n) *****
# True
# **** time = O(n) and space = C *****
# True



		

