# https://leetcode.com/problems/4sum/
# 18. 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.

# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
  # [-1,  0, 0, 1],
  # [-2, -1, 1, 2],
  # [-2,  0, 0, 2]
# ]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        def find(l,r,target,cnt,result,op):
            if r-l+1 < cnt or cnt < 2 or target < nums[l]*cnt or target > nums[r]*cnt:
                return
            if cnt == 2:
                #print(nums[l:r+1])
                my_dict = collections.Counter(nums[l:r+1])
                for i in range(l,r+1):
                    r = target-nums[i]
                    ins = False
                    if r == nums[i]:
                        if my_dict[r] >= 2:
                            ins = True
                    elif r in my_dict:
                        ins = True
                    if ins:
                        t = sorted([nums[i],r])
                        #print(nums[i],r,target,my_dict)
                        op[(tuple(result+t))] = 1
            else:
                for i in range(l,r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        find(i+1,r,target-nums[i],cnt-1,result+[nums[i]],op)
        
        
        nums.sort()
        op = dict()
        find(0,len(nums)-1,target,4,[],op)
        return op
                
                
                
            