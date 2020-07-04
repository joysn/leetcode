# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

   # 1         3     3      2      1
    # \       /     /      / \      \
     # 3     2     1      1   3      2
    # /     /       \                 \
   # 2     1         2                 3

class Solution:
    def numTrees(self, n: int) -> int:
           
        if n <= 1:
            return 1
        op = [0 for i in range(n+1)]
        op[0] = 1
        op[1] = 1
        for i in range(2,n+1):
            temp = 0
            for k in range(1,i+1):
                temp += op[k-1]*op[i-k]
            op[i] = temp
        return op[n]
        
        
            
        