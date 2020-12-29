# https://leetcode.com/problems/insertion-sort-list/
# Sort a linked list using insertion sort.
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
# Algorithm of Insertion Sort:
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #if head.next is None:
        #    return head
        dummy = ListNode(-1)
        curr = head
        while curr:
            curr_next = curr.next
            prv, nxt = dummy, dummy.next
            while nxt:
                if nxt.val > curr.val: break
                prv = nxt
                nxt = nxt.next
            
            curr.next = nxt
            prv.next = curr
            
            curr = curr_next

        return dummy.next