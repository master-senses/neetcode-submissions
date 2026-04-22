"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # visited = set()
        if node is None:
            return None
        if node.neighbors is None:
            return [[]]
        
        adj = {}
        def populate_list(node):
            if node in adj:
                return adj[node]
            copy = Node(node.val)
            adj[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(populate_list(i))
            return copy
            
        
        return populate_list(node)

                
                
        