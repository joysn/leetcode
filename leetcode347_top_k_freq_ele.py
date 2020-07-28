# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a collection counter - collections.Counter(nums)
        # Sort it based on kv[1], i.e. frequency/count
        # sort it descending, so use -kv[1]
        # pickup only first k-1 element, so use [:k]
        # output will be [(freq1,num1), (freq2,num2)]
        # pickup only _[0] for all elements
        return [_[0] for _ in (sorted(collections.Counter(nums).items(), key = lambda kv:(-kv[1], kv[0]))[:k])]