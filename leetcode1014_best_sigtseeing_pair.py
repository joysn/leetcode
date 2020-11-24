# https://leetcode.com/problems/best-sightseeing-pair/
# 1014. Best Sightseeing Pair
# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.
# Example 1:

# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
 
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        i = 0
        mx_score = 0
        for j in range(1,len(A)):
            print(i,j)
            mx_score = max(mx_score,A[j]+A[i]+i-j)
            if A[j]-A[i] + j-i > 0:
                i = j
        return mx_score
        
        
        
        