# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

# Example 1:
# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:

# Input: x = -101
# Output: false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        s = str(x)
        l = len(s)
        
        start = 0
        end = l-1
        mid = floor((l-1)/2)
        
        if l%2 == 0: # Even # of digits
            for i in range(mid+1):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
        else: # Odd # of digits
            for i in range(mid):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
        
        return True
        
# Runtime: 60 ms, faster than 72.09% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 76.53% of Python3 online submissions for Palindrome Number.
        
