# https://leetcode.com/problems/ugly-number-ii/
# 264. Ugly Number II
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

class Solution:
    
    def nthUglyNumber(self, n):
        
        i2,i3,i5 = 0,0,0
        nextMultOf2 = 2
        nextMultOf3 = 3
        nextMultOf5 = 5
        ugly = [1]
        for i in range(n):
            nextNum = min(nextMultOf2,nextMultOf3,nextMultOf5)
            ugly.append(nextNum)
            if nextNum == nextMultOf2:
                i2 += 1
                nextMultOf2 = ugly[i2] *2
            if nextNum == nextMultOf3:
                i3 += 1
                nextMultOf3 = ugly[i3] *3
            if nextNum == nextMultOf5:
                i5 += 1
                nextMultOf5 = ugly[i5] *5
        return ugly[n-1]
                
        
        
        