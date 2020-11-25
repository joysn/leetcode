# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        num_alpha = dict()
        num_alpha[2] = ['a','b','c']
        num_alpha[3] = ['d','e','f']
        num_alpha[4] = ['g','h','i']
        num_alpha[5] = ['j','k','l']
        num_alpha[6] = ['m','n','o']
        num_alpha[7] = ['p','q','r','s']
        num_alpha[8] = ['t','u','v']
        num_alpha[9] = ['w','x','y','z']
        
        
        op = []
        for i in range(len(digits)):
            digit = str(digits)[i]
            if len(op) == 0:
                op = num_alpha[int(digit)]
            else:
                new_op = []
                for e in num_alpha[int(digit)]:
                    t_op = [ele + e for ele in op]
                    new_op += t_op
                op = new_op[:]
        
        return op
        