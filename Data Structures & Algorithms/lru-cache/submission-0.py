class Node:
    def __init__(self, key, val):
        self.prev = None
        self.nxt = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.cache = {} # key is key, value is Node
        self.left.nxt, self.right.prev = self.right, self.left
        self.capacity = capacity
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.nxt, nxt.prev = node, node
        node.nxt, node.prev = nxt, prv
    
    def remove(self, node):
        prv, nxt = node.prev, node.nxt
        prv.nxt, nxt.prev = nxt, prv
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        while len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
        print(self.cache)
        
        

        
