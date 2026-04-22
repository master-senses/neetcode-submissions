class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            if i == 0:
                row = [1] * n
            else:
                row = [0] * n
            grid.append(row)
        for i in range(m):
            grid[i][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        
        return grid[m - 1][n - 1]

        

            