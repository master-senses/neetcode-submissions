from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = []
        adj = defaultdict(list)
        roots = set(i for i in range(numCourses))

        for i in prerequisites:
            if i[1] in roots:
                roots.remove(i[1])
            adj[i[0]].append(i[1])
        
        if not roots:
            # print(adj)
            return []
        print(roots)
        print(adj)
        # print(adj)
        def dfs(node):
            # global path
            if node in visited:
                return False
            if len(adj[node]) == 0:
                if node not in path:
                    path.append(node)
                return True
            visited.add(node)
            
            for i in adj[node]:
                if not dfs(i):
                    return False
            path.append(node)
            adj[node] = []
            visited.remove(node)
            return True
        
        for i in roots:
            if not dfs(i):
                return []
        
        return path
        
        
        

        
        