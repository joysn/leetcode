# https://leetcode.com/problems/shortest-palindrome/submissions/
# 214. Shortest Palindrome
# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
# Example 1:
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: "abcd"
# Output: "dcbabcd"

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        l = len(s)
        
        # Size is 0 or 1
        if l <= 1:
            return s
        
        # The given string itself  is a palindrome
        s_inv = s[::-1]
        if s == s_inv:
            return s
        
        for i in range(l-1,0,-1):
            #print(s[l-1:i-1:-1])
            new_s = s[l-1:i-1:-1]+s
            s_inv = new_s[::-1]
            #print("..",new_s,s_inv)
            if new_s == s_inv:
                return new_s
                        
                
        
        
        
        
        