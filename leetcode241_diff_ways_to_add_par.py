# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

# Example 1:

# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

import re
def diffWaysToCompute(input):
	valid_operators = ['+','-','*']
	
	print(eval(input)) if debug else None
	operands = re.findall('\d+',input)
	operators = re.findall('[+-/*]',input)
	print(operators,operands) if debug else None
	
	op = diffWaysToCompute_helper1(operands,operators)
	return op
	

def diffWaysToCompute_helper1(operands,operators):
	
	
	print("We are here0",operands,operators) if debug else None
	valid_operators = ['+','-','*']
	
	l = len(operands)
	if l == 1:
		print("We are here1",eval(operands[0])) if debug else None
		return tuple([eval(operands[0])])
	if l == 2:
		print("We are here2",eval(operands[0]+operators[0]+operands[1])) if debug else None
		return tuple([eval(operands[0]+operators[0]+operands[1])])
		
	op = []
	op1 = diffWaysToCompute_helper1(operands[1:],operators[1:])
	print("op1",op1) if debug else None
	for e in op1:
		print("Inside op1",operands[0],operators[0],e) if debug else None
		print("We are here 3:",eval(operands[0]+operators[0]+str(e))) if debug else None
		op.append(eval(operands[0]+operators[0]+str(e)))
	print("2",op) if debug else None
	op2 = diffWaysToCompute_helper1(operands[:-1],operators[:-1])
	for e in op2:
		print("Inside op2",e,operators[-1],operands[-1]) if debug else None
		print("We are here 4:",eval(str(e)+operators[-1]+operands[-1])) if debug else None
		op.append(eval(str(e)+operators[-1]+operands[-1]))
	print("3",op) if debug else None
	
	if len(operands[2:]) > 1:
		op3 = diffWaysToCompute_helper1(operands[2:],operators[2:])
		for e in op3:
			print("Inside op3",operands[0],operators[0],operands[1],operators[1],e) if debug else None
			print("We are here 5:",eval(str(eval(operands[0]+operators[0]+operands[1]))),operators[1],str(e)) if debug else None
			op.append(eval(str(eval(operands[0]+operators[0]+operands[1]))+operators[1]+str(e)))
	
	print(op) if debug else None
	return op
	
debug = True
debug = False
# [2, 0]
print(diffWaysToCompute("2-1-1"))
# [-34, -10, -10, 10, -14]
print(diffWaysToCompute("2*3-4*5"))
# [-195, -51, -3, 72, -195]
print(diffWaysToCompute("15-7*6+24"))
print(diffWaysToCompute("1-2+3*4-5"))


cache = dict()
def diffWaysToCompute(input):
	#print("Start with",input)
	l = len(input)
	if input.isdigit():
		return [input]
		
	if input in cache.keys():
		return cache[input]
	
	ret = []
	for idx in range(l):
		if input[idx] in "+-*":
			left = diffWaysToCompute(input[:idx])
			right = diffWaysToCompute(input[idx+1:])
			for l in left:
				for r in right:
					ret.append(eval(str(l)+input[idx]+str(r)))
					#print("To append",eval(str(l)+input[idx]+str(r)))
	#print(ret)
	cache[input] = ret
	return ret

print("####### With Memoization ########")
print("#################################")
cache = dict()
print(diffWaysToCompute("2-1-1"))
# [-34, -10, -10, 10, -14]
cache = dict()
print(diffWaysToCompute("2*3-4*5"))
# [-195, -51, -3, 72, -195]
cache = dict()
print(diffWaysToCompute("15-7*6+24"))
cache = dict()
print(diffWaysToCompute("1-2+3*4-5"))