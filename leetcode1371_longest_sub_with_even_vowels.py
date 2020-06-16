# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
# 1371. Find the Longest Substring Containing Vowels in Even Counts
# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
# Example 1:
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
# O(n^2)

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        debug = False
        l = len(s)
        if l == 0:
            return l
        
        vowels = ['a','e','i','o','u']
        odd_vowel_set = set()
        maxl = 0
        
        for r in range(l):
            odd_vowel_set = set()
            for c in range(r,l):
                if s[c] not in vowels: # Consonant
                    if len(odd_vowel_set) == 0: # All even vowels
                        # We got a okay substring
                        print("Okay Substring",r,c,s[r:c+1],odd_vowel_set) if debug else None
                        if maxl < c-r+1:
                            maxl = c-r+1
                else: # We have vowel
                    if s[c] in odd_vowel_set:
                        odd_vowel_set.remove(s[c])
                        print("Need to remove vowel",s[c],odd_vowel_set) if debug else None
                        if len(odd_vowel_set) == 0: # All even vowels
                            # We got a okay substring
                            print("Okay Substring",r,c,s[r:c+1]) if debug else None
                            if maxl < c-r+1:
                                maxl = c-r+1
                    else:
                        odd_vowel_set.add(s[c])
                        print("Need to add vowel",s[c],odd_vowel_set) if debug else None
                        
        return maxl
