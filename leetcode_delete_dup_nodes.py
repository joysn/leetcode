# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3


class Node:
	def __init__(self,data):
		self.val = data
		self.next = None
		
		
class LinkedList:
	def __init__(self,node):
		self.head = node
		
	def addNode(self,node):
		if self.head is not None:
			curr = self.head
			nxt = self.head.next
			while nxt is not None:
				curr = curr.next
				nxt = nxt.next
			curr.next = node
		else:
			self.head = node
	
	def delNode(self,node):
		if self.head is not None:
			curr = self.head
			while curr.next.next is not None:
				curr = curr.next
			curr.next = None
		else:
			print("Cannot be deleted")
			
			
	def display(self):
		if self.head is None:
			print("Cannot be deleted")
			return
		curr = self.head
		print("Head:",end="")
		while curr is not None:
			print(curr.val,end="->")
			curr = curr.next
		print("End:")
		
		
	def deleteDuplicates1(self):
	
		if self.head is None:
			return self.head
		if self.head.next is None:
			return self.head
		
		op_head = None
		pu = None
		c = self.head
		last_node_to_add = 1
		while c is not None:
			n = c.next
			#print(c.val,"-")
			if n is None:
				last_node_to_add = 1
				break
			#print(n.val,"-")
			
			#print(c.val,n.val)
			if c.val == n.val:
				while c.val == n.val:
					n = n.next
					if n is None:
						last_node_to_add = 0
						break
				c = n
			else: # if c.val != n.val:
				if pu is None:
					pu = c
					op_head = c
					#print("1:",op_head.val)
				elif pu is not None:
					pu.next = c
					pu = c
				c = c.next
			
		if pu is not None and last_node_to_add == 1:
			pu.next = c
		elif pu is None and last_node_to_add == 1:
			pu = c
			op_head = c
		elif pu is not None and last_node_to_add == 0:
			pu.next = None
		
			
		temp = op_head
		print("Output Head:",end="")
		while temp is not None:
			print(temp.val,end="->")
			temp = temp.next
		print("End:")
		return op_head
		
	
debug = False
debug = True
n1 = Node(1)
n2 = Node(2)
n31 = Node(3)
n32 = Node(3)
n41 = Node(4)
n42 = Node(4)
n5 = Node(5)
n6 = Node(6)

ll = LinkedList(n1)
#ll.display()
ll.addNode(n2)
ll.addNode(n31)
ll.addNode(n32)
ll.addNode(n41)
ll.addNode(n42)
ll.addNode(n5)
#ll.addNode(n6)
ll.display()
ll.deleteDuplicates1()


n211 = Node(1)
n212 = Node(1)
n213 = Node(1)
n22 = Node(2)
n23 = Node(3)
 
ll1 = LinkedList(n211)
#ll1.display()
ll1.addNode(n212)
ll1.addNode(n213)
ll1.addNode(n22)
ll1.addNode(n23)
ll1.display()
ll1.deleteDuplicates1()
						
	
#debug = True	
n31 = Node(1)
n321 = Node(2)
n322 = Node(2)
 
ll2 = LinkedList(n31)
#ll1.display()
ll2.addNode(n321)
ll2.addNode(n322)
ll2.display()
ll2.deleteDuplicates1()



#debug = True	
n411 = Node(1)
n412 = Node(1)
n421 = Node(2)
n422 = Node(2)
 
ll3 = LinkedList(n411)
#ll1.display()
ll3.addNode(n412)
ll3.addNode(n421)
ll3.addNode(n422)
ll3.display()
ll3.deleteDuplicates1()


n511 = Node(1)
n512 = Node(1)
 
ll4 = LinkedList(n511)
#ll1.display()
ll4.addNode(n512)
ll4.display()
ll4.deleteDuplicates1()


n611 = Node(1)
n612 = Node(1)
n62 = Node(2)

ll5 = LinkedList(n611)
#ll1.display()
ll5.addNode(n612)
ll5.addNode(n62)
ll5.display()
ll5.deleteDuplicates1()



# (base) D:\>python leetcode_delete_dup_nodes.py
# Head:1->2->3->3->4->4->5->End:
# Output Head:1->2->5->End:
# Head:1->1->1->2->3->End:
# Output Head:2->3->End:
# Head:1->2->2->End:
# Output Head:1->End:
# Head:1->1->2->2->End:
# Output Head:End:
# Head:1->1->End:
# Output Head:End:
# Head:1->1->2->End:
# Output Head:2->End: