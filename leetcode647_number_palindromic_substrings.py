# https://leetcode.com/problems/palindromic-substrings/submissions/
# 647. Palindromic Substrings
# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Note:
# The input string length won't exceed 1000.

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        l = len(s)
        
        if l <= 1:
            return l
        
        cache = [[0 for i in range(l)] for j in range(l)]
        
        count = 0
        for i in range(l):
            cache[i][i] = 1
            count += 1
            
        
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
                    count += 1
                    
        return count