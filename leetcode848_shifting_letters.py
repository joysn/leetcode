# https://leetcode.com/problems/shifting-letters/
# 848. Shifting Letters

# We have a string S of lowercase letters, and an integer array shifts.
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
# Return the final string after all such shifts to S are applied.

# Example 1:
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: 
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.

# "qoqpvw"
# [95,7,67,21,33,23]

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        alphabets_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        
        op = ''
        for idx in range(len(shifts)-2,-1,-1):
            shifts[idx] += shifts[idx+1]
        #print(shifts)
        
        for idx in range(len(S)):
            #print("Char:",S[idx],"Need to shift",shifts[idx], "old pos:",alphabets_dict[S[idx]],"new pos",(alphabets_dict[S[idx]]+shifts[idx])-1,"new alphabet:",alphabets[(alphabets_dict[S[idx]]+shifts[idx])%26-1])
            op += alphabets[(alphabets_dict[S[idx]]+shifts[idx])%26-1]
            
        #print(op)
        
        return op
        