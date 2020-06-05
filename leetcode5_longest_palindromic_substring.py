# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        
        if l <= 1:
            return s
    
        if l == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
            
        cache = [[0 for col in range(l)] for row in range(l)]
        
        for r in range(l):
            cache[r][r] = 1
            
        maxl = 1
        maxstr = s[0]
        for subl in range(1,l):
            for start in range(l-subl):
                end = start + subl
                
                if s[start] == s[end] and subl == 1:
                    cache[start][end] = 1
                elif s[start] == s[end] and cache[start+1][end-1] == 1:
                    cache[start][end] = 1
                else:
                    cache[start][end] = 0
                if cache[start][end] == 1:
                    if maxl < end-start+1:
                        maxl = end-start+1
                        maxstr = s[start:end+1]
                    
        #print(cache)
        #print(maxl)
        #print(maxstr)
        return maxstr