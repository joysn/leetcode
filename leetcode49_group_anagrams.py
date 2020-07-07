# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams
# Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
  # ["ate","eat","tea"],
  # ["nat","tan"],
  # ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = collections.defaultdict(list)
        for word in strs:
            word_dict[tuple(sorted(word))].append(word)
                
        return word_dict.values()