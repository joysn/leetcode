# https://leetcode.com/problems/beautiful-array/
# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)

# Example 1:

# Input: 4
# Output: [2,1,4,3]
# Example 2:
# Input: 5
# Output: [3,1,2,5,4]

# Meaning, no the number should be consecutive

def verify(op):
	for i in range(len(op)-2):
		false = 0
		for k in range(i+1,len(op)-1):
			for j in range(k+1,len(op)):
				print("Testing:***",i,"-",k,"-",j,"***") if debug else None
				if 2*op[k] == op[i]+op[j]:
					print(i,k,j,op[i],op[k],op[j]) if debug else None
					false = 1
					break
			if false == 1:
				return False
		if false == 1:
			return False
	return True

def  beautifulArray(N):
	res=[1]
	while len(res)<N:
		odd=[2*i-1 for i in res]
		even=[2*i for i in res]
		res=odd+even
	op = [i for i in res if i<=N]
	print(verify(op))
	return op
	
debug = True
debug = False
for i in range(11):
	print("For N:",i," The beautiful array is:",beautifulArray(i))
	
# (base) D:\>python leetcode_beautiful_array.py
# True
# For N: 0  The beautiful array is: []
# True
# For N: 1  The beautiful array is: [1]
# True
# For N: 2  The beautiful array is: [1, 2]
# True
# For N: 3  The beautiful array is: [1, 3, 2]
# True
# For N: 4  The beautiful array is: [1, 3, 2, 4]
# True
# For N: 5  The beautiful array is: [1, 5, 3, 2, 4]
# True
# For N: 6  The beautiful array is: [1, 5, 3, 2, 6, 4]
# True
# For N: 7  The beautiful array is: [1, 5, 3, 7, 2, 6, 4]
# True
# For N: 8  The beautiful array is: [1, 5, 3, 7, 2, 6, 4, 8]
# True
# For N: 9  The beautiful array is: [1, 9, 5, 3, 7, 2, 6, 4, 8]
# True
# For N: 10  The beautiful array is: [1, 9, 5, 3, 7, 2, 10, 6, 4, 8]
