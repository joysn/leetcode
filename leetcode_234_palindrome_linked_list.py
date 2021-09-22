# https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return True
        if head.next == None:
            return True
        
        my_list = []
        curr = head
        
        while curr != None:
            my_list.append(curr.val)
            curr = curr.next
        
        #print(my_list)
        
        start = 0
        end = len(my_list) - 1
        while start < end:
            if my_list[start] != my_list[end]:
                return False
            start += 1
            end -= 1
            
        return True
            
        
# 2nd approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         if head == None:
#             return True
#         if head.next == None:
#             return True
        
#         my_list = []
#         curr = head
        
#         while curr != None:
#             my_list.append(curr.val)
#             curr = curr.next
        
#         #print(my_list)
        
#         start = 0
#         end = len(my_list) - 1
#         while start < end:
#             if my_list[start] != my_list[end]:
#                 return False
#             start += 1
#             end -= 1
            
#         return True

        sq=''
        while head:
            sq+=str(head.val)
            head=head.next
        if sq==sq[::-1]:
            return True
        return False
            
       
#3rd Approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return True
        if head.next == None:
            return True
        
        
        # Find the mid point
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        n_head = slow.next
        slow.next = None
        
        
        # Reverse the second part
        reverse_head = n_head
        while n_head.next:
            temp = reverse_head
            reverse_head = n_head.next
            n_head.next = n_head.next.next
            reverse_head.next = temp
            
        while reverse_head:
            if head.val != reverse_head.val:
                return False
            head = head.next
            reverse_head = reverse_head.next
        return True
        
#         if head == None:
#             return True
#         if head.next == None:
#             return True
        
#         my_list = []
#         curr = head
        
#         while curr != None:
#             my_list.append(curr.val)
#             curr = curr.next
        
#         #print(my_list)
        
#         start = 0
#         end = len(my_list) - 1
#         while start < end:
#             if my_list[start] != my_list[end]:
#                 return False
#             start += 1
#             end -= 1
            
#         return True

        # sq=''
        # while head:
        #     sq+=str(head.val)
        #     head=head.next
        # if sq==sq[::-1]:
        #     return True
        # return False
        
    
