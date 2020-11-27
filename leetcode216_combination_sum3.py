# https://leetcode.com/problems/combination-sum-iii/submissions/
# 216. Combination Sum III
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution:
    
    def parse(self,k,n,index,path,res):
        
        #print(index,k,n,path,op)
        if n == 0 and k == 0:
            res.append(path)
        for e in range(index,10):
            #print("...",e,n)
            if e <= n:
                self.parse(k-1,n-e,e+1,path+[e],res)
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res,path,index = [],[],1
        self.parse(k,n,index,path,res)
        return res
        
        
        