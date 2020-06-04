# https://leetcode.com/problems/longest-palindromic-subsequence/
# 516. Longest Palindromic Subsequence
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "bbbab"
# Output: 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input: "cbbd"
# Output: 2
# One possible longest palindromic subsequence is "bb".

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        l = len(s)
        
        if l <= 1:
            return l
        
        if l == 2:
            if s[0] == s[1]:
                return 2
            else:
                return 1
            
        cache = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            cache[i][i] = 1
        
        for subl in range(1,l):
            for start in range(l-subl):
                end = start + subl
                if s[start] == s[end] and subl == 1:
                    cache[start][end] = 2
                elif s[start] == s[end]:
                    cache[start][end] = 2 + cache[start+1][end-1]
                else:
                    cache[start][end] = max(cache[start+1][end],cache[start][end-1])
                
        return cache[0][l-1]