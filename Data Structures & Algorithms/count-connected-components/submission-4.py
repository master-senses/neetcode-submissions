class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        visited = set()
        count = 0

        for node1, node2 in edges:
            if node1 not in adj:
                adj[node1] = []
            if node2 not in adj:
                adj[node2] = []
            
            adj[node1].append(node2)
            adj[node2].append(node1)
        print(adj)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in adj[node]:
                print("child: ", i)
                dfs(i)
            return
        
        for node in adj:
            if node not in visited:
                print("parent: ", node)
                dfs(node)
                count += 1
        
        return count + (n - len(visited))
