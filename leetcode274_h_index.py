# https://leetcode.com/problems/h-index/
# 274. H-Index
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
# Example:
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             # received 3, 0, 6, 1, 5 citations respectively. 
             # Since the researcher has 3 papers with at least 3 citations each and the remaining 
             # two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)    
        count = 0   
        for i in citations:
            if i > count:
                count += 1
        return count
		
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = len(citations)
        
        if l <= 0:
            return l
        
        
        my_hindex = dict()
        
        citations_sorted = sorted(citations)
        
        print(citations_sorted)
        
        for i in citations_sorted:
            for k in my_hindex.keys():
                if k <= i:
                    my_hindex[k] += 1
            if i not in my_hindex.keys():
                my_hindex[i] = 1
                
        print(my_hindex)
        
        op = 0
        for k in my_hindex:
            if min(k,my_hindex[k]) > op:
                op = min(k,my_hindex[k])
                    
        return op