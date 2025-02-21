# Use 2 way linked list to keep recent/least recent but use Dict for lookup in get 

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} 
        # l ptr = LRU /right = recent 
        self.left, self.right = Node(0,0), Node (0,0)
        # point at each other 
        self.left.next, self.right.prev = self.right, self.left

    # Remove value from LIST 
    def removeNode(self, node):
    
    # insert value to right side
    def insertNode(self, node):

    def get(self, key: int) -> int:
        # if exist 
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, at left side key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
