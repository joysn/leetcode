# https://leetcode.com/problems/palindrome-pairs/submissions/
# 336. Palindrome Pairs
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:

# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:

# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def isPalin(string):
            for i in range(len(string)//2):
                if string[i] != string[-(i+1)]:
                    return False
            return True
            
        l = len(words)
        
        my_rev_dict = dict()
        for i in range(l):
            my_rev_dict[words[i][::-1]] = i
        #print(my_rev_dict)
        
        op = []
        for idx in range(l):
            lofword = len(words[idx])
            for i in range(lofword):
                left = words[idx][:i]
                right = words[idx][i:]
                if left in my_rev_dict and isPalin(right) and my_rev_dict[left] != idx:
                    op.append([idx,my_rev_dict[left]])
                    if left == "":
                        op.append([my_rev_dict[left],idx])
                        
                if right in my_rev_dict and isPalin(left) and my_rev_dict[right] != idx:
                    op.append([my_rev_dict[right],idx])
                    if right == "":
                        op.append([idx,my_rev_dict[right]])

        return op
            
        