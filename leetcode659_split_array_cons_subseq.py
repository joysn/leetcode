# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# 659. Split Array into Consecutive Subsequences
# Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5

# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5

# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        l = len(nums)
        
        if l <= 2:
            return False
        
        stack = []
        
        for num in nums:
            if not stack or num > stack[-1][0] + 1:
                stack.append([num,1])
            elif num == stack[-1][0]+1:
                stack[-1][0] += 1
                stack[-1][1] += 1
            else:
                for i in range(len(stack)-1,-1,-1):
                    if num == stack[i][0]+1:
                        stack[i][0] += 1
                        stack[i][1] += 1
                        break
                    elif num > stack[i][0]+1:
                        if stack[i][1] < 3:
                            return False
                        stack.append([num,1])
                        break
                else:
                    stack.append([num,1])
        
        #print(stack)
        for i in range(len(stack)):
            if stack[i][1] < 3:
                return False
        return True
            
            
        
        
        