# https://leetcode.com/problems/redundant-connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
  # 1
 # / \
# 2 - 3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
	
def findRedundantConnection(edges):
	
	op = []
	f_edges = [set(edges[0])]
	for idx in range(1,len(edges)):
		t_edge = set(edges[idx])
		print("For edge",t_edge,f_edges) if debug else None
		new = 1
		merge_idx = -1
		for fe_idx, fe in enumerate(f_edges):
			common_v = fe.intersection(t_edge)
			print("...Compare with",fe," Intersection:",common_v,merge_idx) if debug else None
			if len(common_v) == 2:
				print("...... Found output",common_v) if debug else None
				new = 0
				op = t_edge
			elif len(common_v) == 1:
				print("...... Found Some common",merge_idx) if debug else None
				new = 0
				if merge_idx != -1:
					print(".........Union and Delete",merge_idx) if debug else None
					f_edges[merge_idx] = f_edges[merge_idx].union(fe)
					del f_edges[fe_idx]
					break
				else:
					print(".........Only Merge") if debug else None
					f_edges[fe_idx] = fe.union(t_edge)
					merge_idx = fe_idx
			else:
				continue
		if new == 1:
			f_edges.append(set(t_edge))
				
			
		
	op = list(op)
	print(op) if debug else None
	if len(op) > 1:
		if op[0] > op[1]:
			op = op[::-1]
	print(op) if debug else None
	return op
	
debug = True
debug = False

print(findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3])
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])==[1,4])
print(findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]) == [2,8])
print(findRedundantConnection([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]) == [4,10])
print(findRedundantConnection([[3,7],[1,4],[2,8],[1,6],[7,9],[6,10],[1,7],[2,3],[8,9],[5,9]]) == [8,9])


# (base) D:\>python leetcode_684_redundant_conn.py
# True
# True
# True
# True
# True