# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        l = len(s)
        p_s = s[::-1]
        
        if x < 0:
            p_s = "-"+p_s[:-1]
        print(p_s)
        
        ans = int(p_s)
        if ans > pow(2,31) -1:
            ans = 0
        elif ans < pow(2,31)*-1:
            ans = 0
            
        return(int(ans))
        
        
# Runtime: 48 ms, faster than 17.19% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 43.86% of Python3 online submissions for Reverse Integer.
