# https://leetcode.com/problems/russian-doll-envelopes/
# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:

# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

import copy
def maxEnvelopes_h(envelopes):
	print("Calling with ",envelopes) if debug else None
	l = len(envelopes)
	
	if l == 0:
		print("Return",0,[]) if debug else None
		return 0,[]
	if l == 1:
		print("Return",1,envelopes) if debug else None
		return l,envelopes
		
	if l == 2:
		if envelopes[0][0] < envelopes[1][0] and envelopes[0][1] < envelopes[1][1]:
			print("Return",2,[envelopes[1],envelopes[0]]) if debug else None
			return 2, [envelopes[1],envelopes[0]]
		elif envelopes[1][0] < envelopes[0][0] and envelopes[1][1] < envelopes[0][1]:
			print("Return",2,[envelopes[0],envelopes[1]]) if debug else None
			return 2, [envelopes[0],envelopes[1]]
		else:
			return 0,[]
			
	mx_cnt = 0
	mx_env = []
	for i in range(1,l+1):
		cnt = 0
		cnt,env = maxEnvelopes_h(envelopes[:i-1]+envelopes[i:])
		if cnt != 0:
			print("...",cnt,env,envelopes[i-1]) if debug else None
			if envelopes[i-1][0] > env[0][0] and envelopes[i-1][1] > env[0][1]:
				cnt += 1
				env.insert(0,envelopes[i-1])
		if cnt > mx_cnt:
			mx_cnt = cnt
			mx_env = copy.deepcopy(env)
			
	print("Return",mx_cnt,mx_env) if debug else None
	return mx_cnt,mx_env
		
	

def maxEnvelopes(envelopes) -> int:
	# for i in range(1,len(envelopes)+1):
		# print(envelopes[:i-1]+envelopes[i:])
	# return
	cnt = maxEnvelopes_h(envelopes)[0]
	l = len(envelopes)
	if l > 0 and cnt == 0:
		return 1
	return cnt
	
	
debug = True
debug = False
print("********* Using recrsion ***********")
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])==3)
print(maxEnvelopes([[1,1],[1,1],[1,1]])==1)
# Cannot run
#print(maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]))


cache = dict()
import copy
def maxEnvelopes_h(envelopes):
	print("Calling with ",envelopes) if debug else None
	l = len(envelopes)
	
	if l == 0:
		print("Return",0,[]) if debug else None
		return 0,[]
	if l == 1:
		print("Return",1,envelopes) if debug else None
		return l,envelopes
		
	if l == 2:
		if envelopes[0][0] < envelopes[1][0] and envelopes[0][1] < envelopes[1][1]:
			print("Return",2,[envelopes[1],envelopes[0]]) if debug else None
			return 2, [envelopes[1],envelopes[0]]
		elif envelopes[1][0] < envelopes[0][0] and envelopes[1][1] < envelopes[0][1]:
			print("Return",2,[envelopes[0],envelopes[1]]) if debug else None
			return 2, [envelopes[0],envelopes[1]]
		else:
			return 0,[]
			
	mx_cnt = 0
	mx_env = []
	for i in range(1,l+1):
		cnt = 0
		#cnt,env = maxEnvelopes_h(envelopes[:i-1]+envelopes[i:])
		if cnt != 0:
			print("...",cnt,env,envelopes[i-1]) if debug else None
			if envelopes[i-1][0] > env[0][0] and envelopes[i-1][1] > env[0][1]:
				cnt += 1
				env.insert(0,envelopes[i-1])
		if cnt > mx_cnt:
			mx_cnt = cnt
			mx_env = copy.deepcopy(env)
			
	print("Return",mx_cnt,mx_env) if debug else None
	return mx_cnt,mx_env
		
	

class Env:
	def __init__(self,a,l,b):
		self.a = a
		self.l = l
		self.b = b
		
	def __lt__(self,other):
		if self.a != other.a:
			return self.a < other.a
		elif self.l != other.l:
			return self.l < other.l
		else:
			return self.b < other.b
				
def maxEnvelopes(envelopes) -> int:
	l = len(envelopes)
	
	if l == 0:
		print("Return",0,[]) if debug else None
		return 0
	if l == 1:
		print("Return",1,envelopes) if debug else None
		return l
		
	if l == 2:
		if envelopes[0][0] < envelopes[1][0] and envelopes[0][1] < envelopes[1][1]:
			print("Return",2,[envelopes[1],envelopes[0]]) if debug else None
			return 2
		elif envelopes[1][0] < envelopes[0][0] and envelopes[1][1] < envelopes[0][1]:
			print("Return",2,[envelopes[0],envelopes[1]]) if debug else None
			return 2
		else:
			return 0
		
	#env_list = []
	for e in envelopes:
		e.insert(0,e[0]*e[1])
		#env_list.append(Env(e[0],e[1],e[2]))
	
	print("Before sort",envelopes) if debug else None
	envelopes = sorted(envelopes,reverse=True)
	print("After sort",envelopes) if debug else None

	op_list = [[envelopes[0]]]
	base_list_no = 0
	for i in range(1,l):
		print("For",envelopes[i]) if debug else None
		for base_list_no in range(len(op_list)):
			ins_next_list = 0
			for k in range(len(op_list[base_list_no])):
				if op_list[base_list_no][k][1] > envelopes[i][1] and op_list[base_list_no][k][2] > envelopes[i][2]:
					ins_next_list = 1
					break
			if ins_next_list == 0:
				print("......Could not insert") if debug else None
				op_list[base_list_no].append(envelopes[i])
				break
		if ins_next_list == 1:
			op_list.append([envelopes[i]])
		print("...After list",base_list_no,"The op is",op_list) if debug else None
				
			
	print("After all steps") if debug else None
	for e in op_list: 
		print(e) if debug else None
	print(len(op_list)) if debug else None
	
	return len(op_list)
	
	
debug = True
debug = False
print("********* Using Sequential ***********")
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])==3)
print(maxEnvelopes([[1,1],[1,1],[1,1]])==1)
print(maxEnvelopes([[5,4],[5,3],[4,3],[4,2],[6,7],[6,5],[6,4],[2,12],[2,2]])==4)
print(maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]))
print(maxEnvelopes([[7,8],[12,16],[12,5],[1,8],[4,19],[3,15],[4,10],[9,16]])==3)
print(maxEnvelopes([[8,3],[3,20],[15,5],[11,2],[19,6],[9,18],[1,19],[13,3],[14,20],[6,7]])==4)




def bin_search(q,num):
	
	print("Called bin search with",q,num) if debug else None
	s = 0
	e = len(q) -1
	while s <= e:
		mid = (e-s)//2+s
		print("...",s,mid,e) if debug else None
		if q[mid] == num:
			return mid
		elif q[mid] < num:
			if mid+1 < len(q) and q[mid+1] > num:
				return mid+1
			s = mid + 1
		else:
			if mid == 0:
				return mid
			e = mid - 1
	#return mid

def maxEnvelopes(envelopes) -> int:
	# [h,w]
	# sort the (w) in ascending and (h) in descending
	l = len(envelopes)
	
	if l == 0:
		return 0
	if l == 1:
		return l
		
	print(envelopes) if debug else None
	#let's sort in second property(h)
	envelopes = sorted(envelopes, key= lambda x:(x[1],-x[0]))
	print(envelopes) if debug else None
	
	# then find LIS using first property(w)
	q = [envelopes[0][0]]
	
	for i in range(1, l):
		num = envelopes[i][0]
		if q[-1] < num:
			q.append(num)
		elif q[-1] > num:
			idx = bin_search(q,num)
			print(idx) if debug else None
			q[idx]=num
			
	print(q) if debug else None
	print(len(q)) if debug else None
	return len(q)
	
	
debug = True
debug = False
print("********* Using Bin Search and LIS ***********")
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])==3)
print(maxEnvelopes([[1,1],[1,1],[1,1]])==1)
#debug = True
print(maxEnvelopes([[5,4],[5,3],[4,3],[4,2],[6,7],[6,5],[6,4],[2,12],[2,2]])==4)
print(maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]])==3)
print(maxEnvelopes([[7,8],[12,16],[12,5],[1,8],[4,19],[3,15],[4,10],[9,16]])==3)
print(maxEnvelopes([[8,3],[3,20],[15,5],[11,2],[19,6],[9,18],[1,19],[13,3],[14,20],[6,7]])==4)
print(maxEnvelopes([[17,20],[5,16],[12,17],[14,8],[2,6],[3,9],[6,6],[10,9],[18,3],[19,6],[12,19],[4,2],[3,19],[5,7]])==5)
		
# (base) D:\>python leetcode354_russian_doll.py
# ********* Using recrsion ***********
# True
# True
# ********* Using Sequential ***********
# True
# True
# True
# 3
# True
# True
# ********* Using Bin Search and LIS ***********
# True
# True
# True
# True
# True
# True
# True
		
	
