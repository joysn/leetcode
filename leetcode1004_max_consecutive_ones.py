# https://leetcode.com/problems/max-consecutive-ones-iii/
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s. 
# Example 1:

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:

# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


def maxOnes(A):
	max = 0
	tcount = 0
	for i in range(len(A)):
		#print(i,A[i],tcount,max)
		if A[i] == 1:
			tcount += 1
		else:
			if max < tcount:
				max = tcount
			tcount = 0
	if max < tcount:
		max = tcount
	return max
	
print(maxOnes([1,1,1,0,0,0,1,1,1,1,0]))
print(maxOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]))
		
		
import copy
def longestOnes(A, K):
	print(A,"K count",K) if debug else None
	if K == 0:
		m = maxOnes(A)
		print("returning size",m) if debug else None
		return maxOnes(A)
	l = len(A)
		
	m = 0
	
	no_zeros = 0
	for i in range(K):
		for idx in range(l):
			tempA = []
			tempA = copy.deepcopy(A)
			if A[idx] == 0:
				no_zeros = 1
				lc1 = 0
				if idx == 0:
					if A[idx+1] == 1:
						tempA[idx] = 1
						lc1 = longestOnes(tempA,K-1)
				elif idx == l - 1:
					if A[idx-1] == 1:
						tempA[idx] = 1
						lc1 = longestOnes(tempA,K-1)
				else:
					if A[idx-1] == 1 or A[idx+1] == 1:
						tempA[idx] = 1
						lc1 = longestOnes(tempA,K-1)
				#print("M value and lc1 value",m,lc1)
				if m < lc1:
					m = lc1
	if no_zeros == 0:
		return l
					
	return m
	
debug = False
#debug = True
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([1,1,0,0,1,1,1,0,1,1,0],3))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(longestOnes([0,0,0,1],4))


def longestOnes(A, K):
	print(A,"K count",K) if debug else None
	
	m = 0
	l = len(A)
	count = 0
	for i in range(l):
		if A[i] == 1:
			count += 1
		else:
			if m < count:
				m = count
			count = 0
	if m < count:
		m = count
	# print(Adict) if debug else None
	
	if K == 0:
		# print("returning size",m) if debug else None
		return m
	
	prevOnes = 0
	for i in range(l):
		k = 0
		print("For i",i,"prevOnes",prevOnes) if debug else None
		if A[i] == 0:
			tempCount = prevOnes
			idx = i
			while k < K:
				print("...For K ",k,"with idx",idx,"tempCount",tempCount) if debug else None
				if idx == l:
					break
				if A[idx] == 0:
					tempCount += 1
					k += 1
				else:
					tempCount += 1
				idx += 1
			if idx < l:
				while A[idx] == 1:
					tempCount += 1
					idx += 1
					if idx == l:
						break
			if m < tempCount:
				m = tempCount
			prevOnes = 0
		else:
			prevOnes += 1
				
	return m

print("New method**********")
#debug = True
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([1,1,0,0,1,1,1,0,1,1,0],3))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(longestOnes([0,0,0,1],4))




def longestOnes(A, K):
	print(A,"K count",K) if debug else None
	
	m = 0
	l = len(A)
	count = 0
	start = -1
	oneDict = dict()
	for i in range(l):
		if A[i] == 1:
			if count == 0:
				start = i
			count += 1
		else:
			if start != -1:
				oneDict[start] = count
			start = -1
			if m < count:
				m = count
			count = 0
	if start != -1:
		oneDict[start] = count
	if m < count:
		m = count
	print(oneDict) if debug else None
	
	if K == 0:
		print("returning size",m) if debug else None
		return m
	
	prevOnes = 0
	for i in range(l):
		k = 0
		print("For i",i,"prevOnes",prevOnes) if debug else None
		if A[i] == 0:
			tempCount = prevOnes
			idx = i
			while k < K:
				print("...For K ",k,"with idx",idx,"tempCount",tempCount) if debug else None
				if idx == l:
					break
				if A[idx] == 0:
					tempCount += 1
					k += 1
					idx += 1
				else:
					tempCount += oneDict[idx]
					idx += oneDict[idx]
			if idx < l:
				if idx in oneDict.keys():
					tempCount += oneDict[idx]
					idx += oneDict[idx]
			if m < tempCount:
				m = tempCount
			prevOnes = 0
		else:
			prevOnes += 1
				
	return m

print("New method2**********")
#debug = True
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([1,1,0,0,1,1,1,0,1,1,0],3))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(longestOnes([0,0,0,1],4))



from queue import Queue
def longestOnes(A, K):
	print(A,"K count",K) if debug else None
	
	m = 0
	l = len(A)
	
	q = Queue()
	
	remainingK = K
	for i in range(l):
		if A[i] == 1:
			q.put(A[i])
			print("... After putting 1",q.qsize()) if debug else None
		else:
			if remainingK == 0: # No more 0's can be put
				# Compare with m
				if m < q.qsize():
					m = q.qsize()
				# pop one zero
				while not q.empty():
					tq = q.get()
					print("... After Removing 0",q.qsize()) if debug else None
					if tq == 0:
						remainingK += 1
						break
			if remainingK > 0:
				q.put(A[i])
				remainingK -= 1
				print("... After putting 0",q.qsize())	 if debug else None
					
	if m < q.qsize():
		m = q.qsize()
	#print(q.qsize())
	
				
	return m

print("New method3**********")
#debug = True
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1],0))
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([1,1,0,0,1,1,1,0,1,1,0],3))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(longestOnes([0,0,0,1],4))