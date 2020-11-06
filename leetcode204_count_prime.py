# https://leetcode.com/problems/count-primes/
# 204. Count Primes
# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 0:
            return
        if n <=1:
            return 0
        
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2, n):
            if res[i] == 1:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = 0
        return sum(res)
        