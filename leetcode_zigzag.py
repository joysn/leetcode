# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

import math
def display(op):
	for i in range(len(op)):
		print(op[i])
		
def display_leet(op):
	for i in range(len(op)):
		print(op[i],end='')
	print()
def zigzag(s, numRows):
	rows = numRows
	l = len(s)
	
	if l <= numRows:
		return s
	if numRows == 1:
		return s
	
	no_of_ele_blk = numRows + numRows-2
	no_of_blks = math.ceil(l/no_of_ele_blk)
	print(l,no_of_ele_blk,no_of_blks) if debug else None
	
	op = [[' ' for c in range(no_of_blks*(numRows-1))] for r in range(numRows)]
	# leetcode output
	op_leet = ['' for r in range(numRows)]
	print(op) if debug else None
	
	idx = 0
	blk = 0
	while idx < l:
		for c in range(numRows-1):
			if c == 0:
				for r in range(numRows):
					op[r][blk*(numRows-1)+c] = str(s[idx])
					op_leet[r] += str(s[idx])
					idx += 1
					print("Intermediate") if debug else None
					display(op) if debug else None
					if idx == l:
						print("Final") if debug else None
						display(op)
						display_leet(op_leet)
						return op
				print("One column done") if debug else None
				display(op) if debug else None
			else:
				op[numRows-1-c][blk*(numRows-1)+c] = s[idx]
				op_leet[numRows-1-c] += str(s[idx])
				idx += 1
				print("Intermediate") if debug else None
				display(op) if debug else None
				if idx == 1:
					print("Final") if debug else None
					display(op) 
					display_leet(op_leet)
					return op
		blk += 1
		
	display(op)
	display_leet(op_leet)
	return op
	
debug = False
#debug = True	
zigzag('PAYPALISHIRING',3)
zigzag('PAYPALISHIRING',4)


# (base) D:\>python leetcode_zigzag.py
# ['P', ' ', 'A', ' ', 'H', ' ', 'N', ' ']
# ['A', 'P', 'L', 'S', 'I', 'I', 'G', ' ']
# ['Y', ' ', 'I', ' ', 'R', ' ', ' ', ' ']
# PAHNAPLSIIGYIR
# ['P', ' ', ' ', 'I', ' ', ' ', 'N', ' ', ' ']
# ['A', ' ', 'L', 'S', ' ', 'I', 'G', ' ', ' ']
# ['Y', 'A', ' ', 'H', 'R', ' ', ' ', ' ', ' ']
# ['P', ' ', ' ', 'I', ' ', ' ', ' ', ' ', ' ']
# PINALSIGYAHRPI