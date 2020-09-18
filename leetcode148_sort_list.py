# https://leetcode.com/problems/sort-list/
# 148. Sort List
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
    
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
            
        return self.merge(l, r)
    
    # merge in-place without dummy node
    def merge(self,l,r):
        
        if not l or not r:
            return l or r
        
        if l.val > r.val:
            l,r = r,l
        
        # get the return node "head"
        # also store the pre node, which will iterate
        head = pre = l
        # go to the next item - l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        
        return head
            
        
        