# https://leetcode.com/problems/lru-cache/
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.priority = []
        self.capacity = capacity
        self.curr_capacity = 0
        

    def get(self, key: int) -> int:
        
        if key in self.cache.keys():
            idx = self.priority.index(key)
            del self.priority[idx]
            self.priority.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #print(self.cache)
        if key not in self.cache.keys():
            if len(self.cache) >= self.capacity:
                lpkey = self.priority[0]
                del self.cache[lpkey]
                del self.priority[0]
                self.curr_capacity -= 1

            self.cache[key] = value
            self.priority.append(key)
            self.curr_capacity += 1
        else:
            t = self.get(key)
            self.cache[key] = value
        #print(self.cache)
                
            

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        
        self.capacity = capacity
        # self.curr_capacity = 0
        
        self.priority = []
        self.head = None
        self.tail = None
        
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.key,":",curr.value,end="->")
            curr = curr.next
        print()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            n1 = self.cache[key]
            self.deleteNode(n1)
            self.add(n1)
            return n1.value
        else:
            return -1

        

    def add(self,n1):
        if self.head is None:
            self.head = n1
            self.tail = n1
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = n1
            n1.prev = self.tail
            self.tail = n1
            self.tail.next = None

    def deleteNode(self,n1):

        if n1 == self.head and n1 == self.tail:
            self.head = None
            self.tail = None
        elif n1 == self.head:
            start = self.head
            self.head = start.next
            if self.head is not None:
                self.head.prev = None
            n1.next = None
            n1.prev = None
        elif n1 == self.tail:
            last = self.tail
            prev = last.prev
            prev.next = None
            self.tail = prev
        else:
            n1.prev.next = n1.next
            if n1.next is not None:
                n1.next.prev = n1.prev

        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if len(self.cache) >= self.capacity:
                print("Full Capacity")
                del self.cache[self.head.key]
                self.deleteNode(self.head)
            n1 = Node(key,value)
            self.cache[key] = n1
            self.add(n1)
        else:
            print("Rewrite value")
            self.deleteNode(self.cache[key])
            n1 = Node(key,value)
            self.cache[key] = n1
            self.add(n1)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
