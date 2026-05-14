class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = {}
        n = len(isConnected)
        visited = set()
        count  = 0
        for i in range(n):
            adj[i] = []
        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1:
                    adj[row].append(col)
        # print(adj)

        def dfs(ind):
            if adj[ind] == []:
                return
            visited.add(ind)
            hi = adj[ind]
            adj[ind] = []
            # print(hi)
            for i in hi:
                if i != ind:
                    visited.add(i)
                    dfs(i)
            return
        
        

        for i in adj:
            if len(visited) == n:
                break
            else:
                if i not in visited:
                    dfs(i)
                    count += 1
                    # print(visited)
        
        return count

            


            
