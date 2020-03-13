#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):
	
		l = len(nums)
		hi = l-1
		lo = 0
	
		if l == 0:
			return [-1,-1]
		if l == 1:
			if nums[0] == target:
				return [0,0]
			else:
				return [-1,-1]
            
		if l == 2:
			if nums[0] == target and nums[1] == target:
				return [0,1]
			elif nums[1] == target:
				return [1,1]
			elif nums[0] == target:
				return [0,0]
			else:
				return [-1,-1]
		found = False
		
		lft_idx = None
		rght_idx = None
        
		while hi >= lo:
			mid = int((hi+lo)/2)
			print(hi,lo,mid) if debug else None
			if nums[mid] < target:
				lo = mid+1
			elif nums[mid] > target:
				hi = mid-1
			else: # found
				found = True
				print("Found") if debug else None
				lft_idx = mid
				rght_idx = mid
				for i in range(mid-1,-1,-1):
					if nums[i] == target:
						lft_idx = i
					else:
						break

				for i in range(mid+1,l):
					if nums[i] == target:
						rght_idx = i
					else:
						break
				break
			print("After change",hi,lo) if debug else None
		
		if found:
			return [lft_idx,rght_idx]
		else:
			return [-1,-1]
			
debug = False
print(searchRange([5,7,7,8,8,10],8))
print(searchRange([1,2,3],1))
#debug = True
print(searchRange([1,2,2],2))
print(searchRange([-3,-2,-1],0))