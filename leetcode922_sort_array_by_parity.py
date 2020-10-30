# https://leetcode.com/problems/sort-array-by-parity-ii/
# 922. Sort Array By Parity II
# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.
# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        l = len(A)
        if l%2 != 0:
            return
        
        pos_dict = dict()
        pos_dict[0] = []
        pos_dict[1] = []
        for  i in range(l):
            if i%2 == 0:
                if A[i]%2 == 0:
                    next
                else:
                    pos_dict[0].append(i)
            else:
                if A[i]%2 == 0:
                    pos_dict[1].append(i)
                else:
                    next
                    
        #print(pos_dict)
        for i in range(len(pos_dict[0])):
            temp = A[pos_dict[0][i]]
            A[pos_dict[0][i]] = A[pos_dict[1][i]]
            A[pos_dict[1][i]] = temp
            
        return A
            
        