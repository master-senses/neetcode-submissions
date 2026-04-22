class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = []
        for i in range(len(text1) + 1):
            row = [0] * (len(text2) + 1)
            grid.append(row)
        
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if text1[row - 1] == text2[col - 1]:
                    grid[row][col] = grid[row - 1][col - 1] + 1
                else:
                    grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
        
        return grid[len(text1)][len(text2)]

        
        