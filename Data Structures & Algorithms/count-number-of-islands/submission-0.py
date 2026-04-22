class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def dfs(visited, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0" or (row, col) in visited:
                return
            print(grid[row][col], (row, col))
            visited.add((row, col))
            dfs(visited, row - 1, col)
            dfs(visited, row, col - 1)
            dfs(visited, row + 1, col)
            dfs(visited, row, col + 1)
            

        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in visited or grid[row][col] == "0":
                    continue
                else:
                    count += 1
                    dfs(visited, row, col)
        
        return count
