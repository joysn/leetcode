# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        my_dict = dict()
        
        idx = 0
        l = len(nums)
        while idx < l:
            if nums[idx] in my_dict:
                nums.insert(my_dict[nums[idx]]+1,nums[idx])
                for k in range(nums[idx+1],4):
                    if k in my_dict.keys():
                        my_dict[k] += 1
                del nums[idx+1]
                idx += 1
            else:
                if nums[idx] == 0:
                    for k in my_dict.keys():
                        my_dict[k] += 1
                    my_dict[nums[idx]] = 0
                elif nums[idx] == 1:
                    if 2 in my_dict.keys():
                        my_dict[2] += 1
                    if 0 in my_dict.keys():
                        my_dict[1] = my_dict[0]+1
                    else:
                        my_dict[1] = 0
                else:
                    if 1 in my_dict.keys():
                        my_dict[2] = my_dict[1]+1
                    elif 0 in my_dict.keys():
                        my_dict[2] = my_dict[0]+1
                    else:
                        my_dict[2] = 0
                    
                nums.insert(my_dict[nums[idx]],nums[idx])
                del nums[idx+1]
                idx += 1
            #print("For idx:",idx-1,nums,my_dict)
                
        #print(my_dict)
        #print(nums) 