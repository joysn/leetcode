# https://leetcode.com/problems/search-suggestions-system/
# 1268. Search Suggestions System
# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed. 
# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# Example 2:

# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Example 3:

# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# Example 4:

# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        root,res={},[]
        for word in products:
            node = root
            for ch in word:
                node = node.setdefault(ch,{})
            if '#' in node:
                node['#'].append(word)
            else:
                node['#'] = [word]
				
        def search(node):
            
            ans = []
            nodes = [node]
            while nodes:
                temp = []
                for node in nodes:
                    for key in node:
                        if key == '#':
                            ans += node['#']
                        else:
                            temp.append(node[key])
                nodes = temp
            return sorted(ans)[:3]
            
        node=root
        for w in searchWord:
            if w in node.keys():
                node = node[w]
                res.append(search(node))
            else:
                node = {}
                res.append([])
                
        return res