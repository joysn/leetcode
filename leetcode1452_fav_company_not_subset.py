# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List
# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

# Example 1:
# Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
# Output: [0,1,4] 
# Explanation: 
# Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
# Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
# Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
# Example 2:
# Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
# Output: [0,1] 
# Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
# Example 3:
# Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# Output: [0,1,2,3]


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        my_dict = dict()
        l = len(favoriteCompanies)
        
        for pi in range(l):
            for ci in favoriteCompanies[pi]:
                if ci in my_dict:
                    my_dict[ci].append(pi)
                else:
                    my_dict[ci]= [pi]
                    
        #print(my_dict)
        op = []
        for pi in range(l):
            #print("Person",pi)
            s = set(my_dict[favoriteCompanies[pi][0]])
            #print("Company 0",s)
            for cidx in range(1,len(favoriteCompanies[pi])):
                s = s.intersection(my_dict[favoriteCompanies[pi][cidx]])
                #print("...Company ",cidx,my_dict[favoriteCompanies[pi][cidx]])
            #print("Final set",s)
            if len(s) == 1:
                op.append(pi)
                
        return op