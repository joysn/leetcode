#https://leetcode.com/discuss/interview-question/460127/
# You work on a team whose job is to understand the most sought after toys for the holiday season. A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles. You need to take these quotes and identify which toys are mentioned most frequently. Write an algorithm that identifies the top N toys out of a list of quotes and list of toys.
# Your algorithm should output the top N toys mentioned most frequently in the quotes.

# Input:
# The input to the function/method consists of five arguments:

# numToys, an integer representing the number of toys
# topToys, an integer representing the number of top toys your algorithm needs to return;
# toys, a list of strings representing the toys,
# numQuotes, an integer representing the number of quotes about toys;
# quotes, a list of strings that consists of space-sperated words representing articles about toys

# Output:
# Return a list of strings of the most popular N toys in order of most to least frequently mentioned

# Note:
# The comparison of strings is case-insensitive. If the value of topToys is more than the number of toys, return the names of only the toys mentioned in the quotes. If toys are mentioned an equal number of times in quotes, sort alphabetically.

# Example 1:

# Input:
# numToys = 6
# topToys = 2
# toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
# numQuotes = 6
# quotes = [
# "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
# "The new Elmo dolls are super high quality",
# "Expect the Elsa dolls to be very popular this year, Elsa!",
# "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
# "For parents of older kids, look into buying them a drone",
# "Warcraft is slowly rising in popularity ahead of the holiday season"
# ];

# Output:
# ["elmo", "elsa"]

# Explanation:
# elmo - 4
# elsa - 4
# "elmo" should be placed before "elsa" in the result because "elmo" appears in 3 different quotes and "elsa" appears in 2 different quotes.

# W - total number of words(quotes* words in each quote)
# T - number of toys
# N - max number of toys to return


debug = True
debug = False

import re

# Approach - 1
# Time = O(W) [For loop] + O(TlogT) [Sorting a dictionary of T Size]
# Space = O(T) + O(N)
def getMaxToy1(quotes,toys,N):
	my_op = {toy:[0,0] for toy in toys}
	print(my_op) if debug else None

	for quote in quotes:
		words_list = list(quote.split())
		found_toy = {toy:False for toy in toys}
		#quote_toy = {toy:False for toy in toys}
		#words_list = [word.lower() for word in words_list]
		print("Each quote",words_list) if debug else None
	
		for word in words_list:
			word_lc = word.lower()
			word_lc = re.sub('[^a-z]','',word_lc)
			print(word) if debug else None
			if word_lc in my_op.keys():
				my_op[word_lc][0] += 1
				if found_toy[word_lc] == False:
					my_op[word_lc][1] += 1
				found_toy[word_lc] = True
				
	print(my_op) if debug else None

	#print([v for v in sorted(my_op.items(), key=lambda item: item[1][0],reverse=True)])
	return([v for v in sorted(my_op.items(), key=lambda item: (-item[1][0],-item[1][1]))][:N])
	

# Approach - 1
# Time = O(W) [For loop] + O(TlogN) [Maintaining heap of size T]
# Space = O(T) + O(N)

from heapq import heappush, heappop

class Toy:
	def __init__(self,count, quote_count, toy_name):
		self.toy_name = toy_name
		self.count = count
		self.quote_count = quote_count
		
		
	def __lt__(self,other):
		if self.count != other.count:
			return self.count<other.count
		elif self.quote_count != other.quote_count:
			return self.quote_count < other.quote_count
		else:
			self.toy_name > self.toy_name			
		
def getMaxToy2(quotes,toys,N):

	my_op = {toy:[0,0] for toy in toys}
	print(my_op) if debug else None

	for quote in quotes:
		words_list = list(quote.split())
		found_toy = {toy:False for toy in toys}
		#quote_toy = {toy:False for toy in toys}
		#words_list = [word.lower() for word in words_list]
		print("Each quote",words_list) if debug else None
	
		for word in words_list:
			word_lc = word.lower()
			word_lc = re.sub('[^a-z]','',word_lc)
			print(word) if debug else None
			if word_lc in my_op.keys():
				my_op[word_lc][0] += 1
				if found_toy[word_lc] == False:
					my_op[word_lc][1] += 1
				found_toy[word_lc] = True
				
	print(my_op) if debug else None
	
	sorted_op = []
	for toy in my_op.keys():
		t = Toy(my_op[toy][0],my_op[toy][1],toy)
		heappush(sorted_op,t)
		if len(sorted_op) > N:
			heappop(sorted_op)
		
		
	op = []
	for i in range(len(sorted_op)):
		op.append(heappop(sorted_op).toy_name)
	
	print(op[::-1]) if debug else None
	return op[::-1]
	
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
N=3

print(getMaxToy1(quotes,toys,N))
print(getMaxToy2(quotes,toys,N))



	
	
	
