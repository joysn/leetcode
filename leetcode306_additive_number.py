# https://leetcode.com/problems/additive-number/
# 306. Additive Number
# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

# Example 1:
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             # 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
             # 1 + 99 = 100, 99 + 100 = 199

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        l = len(num)
        if l < 3:
            return False
        
        for i in range(l): # get all a's
            a = num[:i+1]
            if a != '0' and a.startswith('0'): break
            num1 = int(a)
            for j in range(i+1,l): # get all b's
                b = num[i+1:j+1]
                if b != '0' and b.startswith('0'): break
                num2 = int(b)
                add_num = [num1,num2]
                #print(num1,num2)
                k = j + 1
                while k < l:
                    c = add_num[-1] + add_num[-2]
                    cS = str(c)
                    if num[k:].startswith(cS):
                        k += len(cS)
                        add_num.append(c)
                    else:
                        break
                else:
                    if len(add_num) >= 3:
                        return True
        return False