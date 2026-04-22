class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        adj = {}
        visited = set()
        root = edges[0][0]
        for node1, node2 in edges:
            if node1 not in adj:
                adj[node1] = []
            
            if node2 not in adj:
                adj[node2] = []

            adj[node1].append(node2)
            adj[node2].append(node1)

        def cyclic(prev, node):
            if node in visited:
                return False
            visited.add(node)
            for i in adj[node]:
                if i != prev:
                    if not cyclic(node, i):
                        return False
            return True
            
        if cyclic(None, root) and len(visited) == n:
            return True
        
        return False


