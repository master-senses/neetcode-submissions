class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_LEN = len(grid)
        COL_LEN = len(grid[0])
        visited = set()
        count = 0
        def dfs(row, col):
            if row >= ROW_LEN or row < 0 or col >= COL_LEN or col < 0 or (row, col) in visited:
                return
            if grid[row][col] == "0":
                return 
            print(row, col)
            grid[row][col] = "0"
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return
        
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                # print(grid)
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
                    print(grid)
        
        return count