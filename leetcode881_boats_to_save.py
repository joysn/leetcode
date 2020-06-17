# https://leetcode.com/problems/boats-to-save-people/
# 881. Boats to Save People
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

## O(n*l)
def numRescueBoats(people, limit: int) -> int:
        
	debug = False
	l = len(people)
	if l <= 1:
		return l
	
	people = sorted(people,reverse=True)
	boats = [0 for i in range(limit+1)]
	boats[limit] = l
	print(boats) if debug else None
	count = 0
	for i in range(l):
		print("Considering people with weight",people[i]) if debug else None
		for wt in range(people[i],limit+1):
			print("...Weight is",wt) if debug else None
			if boats[wt] > 0 :
				if wt == limit:
					boats[wt] -= 1
					boats[wt-people[i]] += 1
				else:
					boats[wt] -= 1
					count += 1
				break
		print(boats) if debug else None
	print(boats) if debug else None
        
	for i in range(limit):
		if boats[i] > 0:
			count += boats[i]
	return count
	
print(numRescueBoats([3,2,3,2,2],6)==3)
print(numRescueBoats([1,2],3)==1)
print(numRescueBoats([3,1,2],3)==2)
print(numRescueBoats([3,1,2,2],3)==3)
print(numRescueBoats([3,5,3,4],5)==4)
        
# O(N)	
def numRescueBoats(people, limit: int) -> int:
        
	l = len(people)
	if l <= 1:
		return l
	
	count = 0
	people = sorted(people,reverse=True)
	
	print(people) if debug else None
	wt_dict = dict()
	for i in range(l):
		if people[i] in wt_dict.keys():
			wt_dict[people[i]] += 1
		else:
			wt_dict[people[i]] = 1
	
	print(wt_dict) if debug else None
	
	for i in range(l):
		if people[i] in wt_dict.keys():
			print("For weight",people[i]) if debug else None
			count += 1
			wt_dict[people[i]] -= 1
			wt_left = limit - people[i]
			if wt_dict[people[i]] == 0:
				del wt_dict[people[i]]
			if wt_left != 0:
				second_person = wt_left
				while second_person != 0:
					if second_person in wt_dict.keys():
						wt_dict[second_person] -= 1
						if wt_dict[second_person] == 0:
							del wt_dict[second_person]
						break
					else:
						second_person -= 1
		print(wt_dict, count) if debug else None
	
	return count
	
debug = False
print("#############O(N)##############")
print(numRescueBoats([1,2],3)==1)
print(numRescueBoats([3,1,2],3)==2)
print(numRescueBoats([3,1,2,2],3)==3)
print(numRescueBoats([3,5,3,4],5)==4)
print(numRescueBoats([3,2,3,2,2],6)==3)
        