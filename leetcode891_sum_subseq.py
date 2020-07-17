# https://leetcode.com/problems/sum-of-subsequence-widths/
# 891. Sum of Subsequence Widths
# Given an array of integers A, consider all non-empty subsequences of A.
# For any sequence S, let the width of S be the difference between the maximum and minimum element of S.
# Return the sum of the widths of all subsequences of A. 
# As the answer may be very large, return the answer modulo 10^9 + 7.
# Example 1:
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# Note:
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        
        
        # Explaination - Input [4,2,3,1]
        # After sorting [1,2,3,4]
        # All Subsequences are
        # 1,2,3,4,12,13,14,23,24,34,123,124,134,234,1234
        # 1-1   2-2   3-3    4-4
        #
        #       2-1   3-1    4-1
        #             3-2    4-2
        #                    4-3
        #
        #             3-1    4-1
        #                    4-1
        #                    4-2
        #
        #                    4-1
        #
        # 1* 2 power 0 - 1* 2 power 3
        # 2* 2 power 1 - 2* 2 power 2
        # 3* 2 power 2 - 3* 2 power 1
        # 4* 2 power 3 - 4* 2 power 0
        
        l = len(A)
        A.sort()    
        res=0
        for i in range(l):
            res+=(A[i]<<i)-(A[i]<<(l-i-1))
        return res%(10**9+7)