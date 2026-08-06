from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        path = []
        visited = set()
        adj = defaultdict(list)
        roots = set(i for i in range(numCourses))

        for i in prerequisites:
            # if i[1] in roots:
            #     roots.remove(i[1])
            adj[i[0]].append(i[1])
        
        # if not roots:
        #     # print(adj)
        #     return []
        # print(roots)
        # print(adj)
        # print(adj)
        def dfs(node):
            # global path
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for i in adj[node]:
                if not dfs(i):
                    return False
            path.append(node)
            adj[node] = []
            cycle.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return path
        
        
        

        
        