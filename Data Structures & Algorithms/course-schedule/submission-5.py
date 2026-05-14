class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for pair in prerequisites:
            adj[pair[0]].append(pair[1])
        
        def dfs(visited, node):
            if len(adj[node]) == 0:
                return True
            if node in visited:
                # print("node is in visited", visited, node)
                return False
            visited.add(node)
            
            for i in adj[node]:
                if not dfs(visited, i):
                    # print(node)
                    return False
            visited.remove(node)
            return True
        # print(adj)
        for i in range(numCourses):
            visited = set()
            if not dfs(visited, i):
                return False
        
        return True


                