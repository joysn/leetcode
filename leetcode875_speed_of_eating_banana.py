# https://leetcode.com/problems/koko-eating-bananas/
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.
# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
# Note:
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

import math
def minEatingSpeed(piles, H):
	if H == 0: # Not possible
		return 
	
	l = len(piles)
	if H < l: # not possible
		return 
	max_p = max(piles)
	min_p = min(piles)
	if H == l:
		return max_p
		
	# H > l
	total = sum(piles)
	
	lo = math.floor(total/H)
	hi = max_p
	
	while lo < hi:
		mid = (lo+hi)//2
		print("Trial Speed between",lo,"and",hi,"is",mid) if debug else None
		if mid == 0:
			lo = 1
			break
		h_count = 0
		for e in piles:
			h_count += math.ceil(e/mid)
			print(math.ceil(e/mid),e/mid) if debug else None
		print("Got Count",h_count) if debug else None
		if h_count > H:
			print("h_count is more") if debug else None
			lo = mid+1
		else:
			print("h_count is less or equal") if debug else None
			hi = mid
			
	print(lo,mid,hi)
	return lo

debug = True
debug = False	
for i in range(9):
	print(i,"Hours, Min Speed",minEatingSpeed([3,6,7,11],i))
print(minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],823855818))
print(minEatingSpeed([312884470],968709470))

# (base) D:\>python leetcode_speed_of_eating_banana.py
# 0 Hours, Min Speed None
# 1 Hours, Min Speed None
# 2 Hours, Min Speed None
# 3 Hours, Min Speed None
# 4 Hours, Min Speed 11
# 5 Hours, Min Speed 7
# 6 Hours, Min Speed 6
# 7 Hours, Min Speed 6
# 8 Hours, Min Speed 4
# 14
# 1