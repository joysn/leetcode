# https://leetcode.com/problems/lfu-cache/
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
# Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

# Follow up:
# Could you do both operations in O(1) time complexity?
# Example:
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.priority = []
        

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            val,u = self.cache[key]
            self.put(key,val)
            return val
        else:
            return -1
        
    def add(self,key,u):
        if len(self.priority) == 0:
            self.priority.append(key)
        else:
            i = 0
            while i < len(self.priority):
                #print(i,self.priority[i], self.cache[self.priority[i]])
                if self.cache[self.priority[i]][1] <= u:
                    #print("Here")
                    i += 1
                else:
                    break
            self.priority.insert(i,key)
    

    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0:
            return
        if key not in self.cache.keys():
            # Insert
            if len(self.cache) >= self.capacity:
                # delete
                del self.cache[self.priority[0]]
                del self.priority[0]
            # Insert
            self.cache[key] = (value,1)
            # Insert at correct position based on usage - Usage is 1
            self.add(key,1)
        else:
            # Update
            idx = self.priority.index(key)
            del self.priority[idx]
            usage = self.cache[key][1]
            usage += 1
            # insert at correct position
            self.add(key,usage)
            self.cache[key] = (value,usage)
        #print(self.cache, self.priority)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)